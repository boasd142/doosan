import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy, QoSDurabilityPolicy, QoSLivelinessPolicy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
import math
from decimal import Decimal, getcontext

class MoveToUncertainArea(Node):
    def __init__(self):
        super().__init__('move_to_uncertain_area')

        # Decimal 연산의 정밀도를 설정 (예: 10자리)
        getcontext().prec = 1

        # /map 토픽 구독
        self.map_subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10
        )

        # /odom 토픽 구독
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1,
            durability=QoSDurabilityPolicy.VOLATILE,
            lifespan=rclpy.duration.Duration(seconds=0),
            deadline=rclpy.duration.Duration(seconds=0),
            liveliness=QoSLivelinessPolicy.AUTOMATIC,
            liveliness_lease_duration=rclpy.duration.Duration(seconds=0)
        )
        self.odom_subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            qos_profile
        )

        # navigate_to_pose 액션 클라이언트
        self.client = ActionClient(self, NavigateToPose, '/navigate_to_pose')

        # 로봇 위치 변수
        self.current_position = None

        # 불확실한 지역 좌표
        self.uncertain_areas = []

        # 실행 중에 새로운 명령을 방지하는 플래그
        self.is_executing = False

    def odom_callback(self, msg: Odometry):
        # Decimal을 사용하여 로봇의 현재 위치를 업데이트
        if msg.pose.pose.position:
            self.current_position = (
                Decimal(msg.pose.pose.position.x),
                Decimal(msg.pose.pose.position.y)
            )

    def map_callback(self, msg: OccupancyGrid):
        if self.is_executing:
            # 실행 중에는 새로운 명령을 무시함
            return

        # 맵에서 불확실한 지역(-1)을 찾음
        width = msg.info.width
        height = msg.info.height
        resolution = Decimal(msg.info.resolution)  # 해상도를 Decimal로 사용
        origin_x = Decimal(msg.info.origin.position.x)
        origin_y = Decimal(msg.info.origin.position.y)

        self.uncertain_areas.clear()
        for i in range(height):
            for j in range(width):
                idx = i * width + j
                if msg.data[idx] == -1:
                    x = origin_x + j * resolution
                    y = origin_y + i * resolution

                    # 로봇과 2미터 이내의 거리에 있는지 확인 (거리 계산 시 Decimal 사용)
                    if self.current_position:
                        dist = Decimal(math.sqrt((x - self.current_position[0])**2 + (y - self.current_position[1])**2))
                        if dist <= 2.0:
                            self.uncertain_areas.append((x, y, dist))

        if self.uncertain_areas:
            # 거리가 가까운 순으로 정렬 (내림차순)
            self.uncertain_areas.sort(key=lambda area: area[2], reverse=True)
            self.get_logger().info(f"2미터 이내의 불확실한 지역 {len(self.uncertain_areas)}개를 찾았습니다.")
            # 가장 가까운 불확실한 지역으로 이동
            self.move_to_uncertain_area(self.uncertain_areas.pop(0))
        else:
            self.get_logger().info("2미터 이내에 불확실한 지역이 없습니다.")

    async def move_to_uncertain_area(self, target):
        if self.current_position is None:
            self.get_logger().info("현재 위치를 알 수 없습니다.")
            return

        if not self.client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info("액션 서버가 사용할 수 없습니다!")
            return

        self.is_executing = True  # 실행 플래그 설정

        target_pose = PoseStamped()
        target_pose.header.frame_id = 'map'
        target_pose.header.stamp = self.get_clock().now().to_msg()
        target_pose.pose.position.x = target[0]
        target_pose.pose.position.y = target[1]
        target_pose.pose.orientation.w = 1.0

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = target_pose

        self.get_logger().info(f"{target[:2]}로 이동을 시도합니다.")

        # 비동기적으로 goal을 보냄
        goal_handle = await self.client.send_goal_async(goal_msg)

        if goal_handle.accepted:
            self.get_logger().info("목표가 수락되었습니다.")
            # 비동기적으로 결과를 기다림
            result = await goal_handle.get_result_async()
            self.result_callback(result)
        else:
            self.get_logger().info("목표가 거부되었습니다. 다음 목표를 시도합니다.")
            self.is_executing = False
            if self.uncertain_areas:
                await self.move_to_uncertain_area(self.uncertain_areas.pop(0))

    def result_callback(self, result):
        # 목표 성공 여부 확인
        if result.status != 3:  # 목표에 성공적으로 도달하지 못한 경우
            self.get_logger().info("목표에 도달하지 못했습니다. 다음 목표를 시도합니다.")
            if self.uncertain_areas:
                self.move_to_uncertain_area(self.uncertain_areas.pop(0))
        else:
            self.get_logger().info("목표에 성공적으로 도달했습니다.")

        # 플래그 리셋
        self.is_executing = False

        # 새로운 불확실한 지역을 찾기 위해 재검색
        self.get_logger().info("불확실한 지역을 재검색합니다.")

        # 탐색할 지역이 더 있으면 다시 시도
        if self.uncertain_areas:
            self.move_to_uncertain_area(self.uncertain_areas.pop(0))

def main(args=None):
    rclpy.init(args=args)
    move_node = MoveToUncertainArea()
    rclpy.spin(move_node)

    move_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
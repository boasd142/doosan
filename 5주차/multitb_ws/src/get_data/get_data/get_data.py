import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Quaternion, PoseStamped, Point
from nav2_msgs.action import NavigateToPose
from nav_msgs.msg import Odometry
from rclpy.action import ActionClient
from std_msgs.msg import Int32

class GETINFO(Node):
    def __init__(self):
        super().__init__('getinfo')

        # Action Client 초기화
        self.action_client_nav = ActionClient(self, NavigateToPose, '/tb2/navigate_to_pose')

        # 구독 설정
        self.subscriptions_theif = self.create_subscription(
            Int32,
            'thief_spawn',
            self.thief_callback,
            10
        )
        self.subscriptions_detect = self.create_subscription(
            Point,
            'thief_point_up',
            self.thief_position_callback,
            10
        )

        # 변수 초기화
        self.thief_status = 0
        self.thief_position = None

    def thief_callback(self, msg):
        if msg.data == 1:
            self.thief_status = 1
        
        if self.thief_status == 1:
            self.get_logger().info(f'Thief status updated: {self.thief_status}')
            self.move_to_thief()  # 상태 업데이트 시 이동 시도
        else:
            return

    def thief_position_callback(self, msg):
        self.thief_position = msg
        self.get_logger().info(f'Thief position received: x={msg.x}, y={msg.y}')
        self.move_to_thief()  # 위치 업데이트 시 이동 시도

    def move_to_thief(self):
        if self.thief_status == 1:
            if self.thief_position is not None:
                self.get_logger().info('Sending goal to thief position...')
                self.send_goal(self.thief_position.x, self.thief_position.y)
            else:
                self.get_logger().info('Thief detected, but position not received yet.')
        elif self.thief_status == 0:
            self.thief_position = None
            self.send_goal(-5.0, 7.0)
            self.get_logger().info('No thief detected.')
            
    def send_goal(self, x, y, yaw=0.0):
        # 목표 위치 생성
        waypoint = PoseStamped()
        waypoint.header.frame_id = 'map'
        waypoint.header.stamp = self.get_clock().now().to_msg()

        waypoint.pose.position.x = x
        waypoint.pose.position.y = y
        waypoint.pose.position.z = 0.0

        # Orientation 설정 (yaw 사용)
        waypoint.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)

        # Goal 메시지 생성 및 전송
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = waypoint

        self._send_goal_future = self.action_client_nav.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected.')
            return

        self.get_logger().info('Goal accepted.')
        self._goal_handle = goal_handle
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result()
        if result is not None:
            self.get_logger().info(f'Goal completed with status: {result.status}')
        else:
            self.get_logger().warning('Goal failed.')

def main(args=None):
    rclpy.init(args=args)
    getinfo = GETINFO()
    rclpy.spin(getinfo)

if __name__ == '__main__':
    main()

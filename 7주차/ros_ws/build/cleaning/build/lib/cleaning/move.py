# import rclpy, math, numpy
# from rclpy.node import Node
# from rclpy.action import ActionClient
# from nav2_msgs.action import NavigateToPose
# from rclpy.action.client import GoalStatus
# from geometry_msgs.msg import PoseStamped
# from nav_msgs.msg import Odometry
# from decimal import Decimal
# from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy, QoSLivelinessPolicy

# # from sensor_msgs.msg import LaserScan
# # from nav_msgs.msg import OccupancyGrid
# # import numpy as np

# class Move(Node):
#     def __init__(self):
#         super().__init__('move')

#         qos_profile = QoSProfile(
#             reliability=QoSReliabilityPolicy.BEST_EFFORT,  # 신뢰성: BEST_EFFORT
#             history=QoSHistoryPolicy.KEEP_LAST,            # 히스토리 정책: KEEP_LAST
#             depth=1,                                       # 큐 크기: 1
#             durability=QoSDurabilityPolicy.VOLATILE,       # 지속성: VOLATILE
#             lifespan=rclpy.duration.Duration(seconds=0),   # Lifespan: Infinite (기본값)
#             deadline=rclpy.duration.Duration(seconds=0),   # Deadline: Infinite (기본값)
#             liveliness=QoSLivelinessPolicy.AUTOMATIC,      # Liveliness: AUTOMATIC
#             liveliness_lease_duration=rclpy.duration.Duration(seconds=0)  # Liveliness lease duration: Infinite
#         )

#         # navigate_to_pose 액션 클라이언트
#         self.client = ActionClient(
#             self,
#             NavigateToPose,
#             '/navigate_to_pose'
#         )

#         # /odom 토픽 구독 (로봇의 위치 정보)
#         self.pose_subscription = self.create_subscription(
#             Odometry,
#             '/odom',  # 로봇의 위치를 받는 토픽 (Odometry 사용)
#             self.pose_callback,
#             qos_profile = qos_profile
#         )

#         #  # /scan 서브스크라이브
#         # self.scan_subscription = self.create_subscription(
#         #     LaserScan,
#         #     '/scan',  # 라이더 데이터가 퍼블리시되는 토픽
#         #     self.scan_callback,
#         #     10  # 큐 사이즈
#         # )

#         # # 왼쪽 빈공간 거리
#         # self.left_distance = 0.0
#         # # 전진 빈공간 거리
#         # self.center_distance = 0.0
#         # # 오른쪽 빈공간 거리
#         # self.right_distance = 0.0

#         self.certain_areas = [
#             [0.0, 0.0], [0.0, 0.1], [0.0, 0.2], [0.0, 0.3], [0.0, 0.4], [0.0, 0.5], [0.0, 0.6], [0.0, 0.7], [0.0, 0.8], [0.0, 0.9],
#             [0.1, 0.0], [0.1, 0.1], [0.1, 0.2], [0.1, 0.3], [0.1, 0.4], [0.1, 0.5], [0.1, 0.6], [0.1, 0.7], [0.1, 0.8], [0.1, 0.9],
#             [0.2, 0.0], [0.2, 0.1], [0.2, 0.2], [0.2, 0.3], [0.2, 0.4], [0.2, 0.5], [0.2, 0.6], [0.2, 0.7], [0.2, 0.8], [0.2, 0.9],
#             [0.3, 0.0], [0.3, 0.1], [0.3, 0.2], [0.3, 0.3], [0.3, 0.4], [0.3, 0.5], [0.3, 0.6], [0.3, 0.7], [0.3, 0.8], [0.3, 0.9],
#             [0.4, 0.0], [0.4, 0.1], [0.4, 0.2], [0.4, 0.3], [0.4, 0.4], [0.4, 0.5], [0.4, 0.6], [0.4, 0.7], [0.4, 0.8], [0.4, 0.9],
#             [0.5, 0.0], [0.5, 0.1], [0.5, 0.2], [0.5, 0.3], [0.5, 0.4], [0.5, 0.5], [0.5, 0.6], [0.5, 0.7], [0.5, 0.8], [0.5, 0.9],
#             [0.6, 0.0], [0.6, 0.1], [0.6, 0.2], [0.6, 0.3], [0.6, 0.4], [0.6, 0.5], [0.6, 0.6], [0.6, 0.7], [0.6, 0.8], [0.6, 0.9],
#             [0.7, 0.0], [0.7, 0.1], [0.7, 0.2], [0.7, 0.3], [0.7, 0.4], [0.7, 0.5], [0.7, 0.6], [0.7, 0.7], [0.7, 0.8], [0.7, 0.9],
#             [0.8, 0.0], [0.8, 0.1], [0.8, 0.2], [0.8, 0.3], [0.8, 0.4], [0.8, 0.5], [0.8, 0.6], [0.8, 0.7], [0.8, 0.8], [0.8, 0.9],
#             [0.9, 0.0], [0.9, 0.1], [0.9, 0.2], [0.9, 0.3], [0.9, 0.4], [0.9, 0.5], [0.9, 0.6], [0.9, 0.7], [0.9, 0.8], [0.9, 0.9]
#         ]

#         # 청소한 지역
#         self.clean_areas = []

#         # 로봇 위치 초기화
#         self.robot_position = [0,0]

#         # 청소 알고리즘
#         self.move_to_dirty_area(self.robot_position)


#     # def scan_callback(self, msg: LaserScan):
#     #     self.left_distance = msg.ranges[int(len(msg.ranges)*(2/4))]
#     #     self.center_distance = msg.ranges[int(len(msg.ranges)*(1/4))]
#     #     self.right_distance = msg.ranges[int(len(msg.ranges))-1]

#     #     # self.get_logger().info(f"{self.left_distance}")
#     #     # self.get_logger().info(f"{self.center_distance}")
#     #     # self.get_logger().info(f"{self.right_distance}")
    

#     def pose_callback(self, msg: Odometry):
#         # 로봇의 현재 위치를 받아옴 (맵 좌표계에서의 x, y 위치)
#         self.robot_position = [float(Decimal(msg.pose.pose.position.x).quantize(Decimal('0.1'))), float(Decimal(msg.pose.pose.position.y).quantize(Decimal('0.1')))]

#         # 목표 지점 범위 내의 지점 추가
#         self.get_logger().info('청소 지점 저장')
#         self.add_visited_area(self.robot_position)


#     def move_to_dirty_area(self, target):
#         # navigate_to_pose 액션 클라이언트 사용
#         if not self.client.wait_for_server(timeout_sec=1.0):
#             self.get_logger().info("Action server not available!")
#             return

#         # 목표 위치 설정 (PoseStamped 사용)
#         target_pose = PoseStamped()
#         target_pose.header.frame_id = 'map'  # 맵 좌표계 사용
#         target_pose.header.stamp = self.get_clock().now().to_msg()
#         target_pose.pose.position.x = target[0]
#         target_pose.pose.position.y = target[1]
#         target_pose.pose.orientation.w = 1.0  # 회전 각도 설정 (기본값으로 회전하지 않음)

#         # 액션 목표 설정
#         goal_msg = NavigateToPose.Goal()
#         goal_msg.pose = target_pose

#         # 액션 서버로 목표 전송
#         self.get_logger().info(f"목표지점으로 이동: {target}")
#         self.send_goal_future = self.client.send_goal_async(goal_msg)
#         self.send_goal_future.add_done_callback(self.navigate_to_pose_action_goal)


#     def navigate_to_pose_action_goal(self, future):
#         goal_handle = future.result()
        
#         if not goal_handle.accepted:
#             self.get_logger().warning('목표지점 설정 거부')
#             return
        
#         action_result_future = goal_handle.get_result_async()
#         action_result_future.add_done_callback(self.navigate_to_pose_action_result)


#     def navigate_to_pose_action_result(self, future):
#         action_status = future.result().status
#         #action_result = future.result().result
        
#         if action_status == GoalStatus.STATUS_SUCCEEDED:
#             # 가장 가까운 지점 찾기
#             self.get_logger().info('다음 목표 지점 설정')
#             self.move_to_dirty_area(self.get_close_area())

#         else:
#             self.get_logger().warning('목표 지점에 도달하지 못했습니다.') 

#     def get_close_area(self):
#         # 가장 멀리 있는 확실한 지역 찾기
#         min_distance = 10
#         closest_area = None

#         for i in range(len(self.certain_areas)):
#             area = self.certain_areas[i]

#             if area not in self.clean_areas:
#                 # 가장 가까운 지역 찾기
#                 distance = math.sqrt((area[0] - self.robot_position[0]) ** 2 + (area[1] - self.robot_position[1]) ** 2)
#                 if distance < min_distance:
#                     min_distance = distance
#                     closest_area = area

#         if closest_area is not None:
#             return closest_area
        
#         elif closest_area is None:
#             self.get_logger().info("청소 완료")
            
#             return


#     def add_visited_area(self, target):
#         # 현재 위치의 범위에 해당하는 좌표들 추가        
#         for dx in numpy.arange(-0.8, 0.8, 0.1):
#             for dy in numpy.arange(-0.8, 0.8, 0.1):
#                 visited_area = [float(Decimal(target[0] + dx).quantize(Decimal('0.1'))), float(Decimal(target[1] + dy).quantize(Decimal('0.1')))]
#                 if visited_area not in self.visit_areas:
#                     self.visit_areas.append(visited_area)


# def main(args=None):
#     rclpy.init(args=args)
#     move_node = Move()

#     rclpy.spin(move_node)

#     move_node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
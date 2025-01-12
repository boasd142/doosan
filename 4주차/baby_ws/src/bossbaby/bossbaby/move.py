import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Quaternion, PoseStamped
from nav2_msgs.srv import SetInitialPose
from nav2_msgs.action import NavigateToPose, FollowWaypoints
from rclpy.action import ActionClient
from std_msgs.msg import String
from geometry_msgs.msg import Point


class GoalPublisher(Node):
    def __init__(self):
        super().__init__('goal_publisher')
        # NavigateToPose 액션 클라이언트
        self.action_client_nav = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        # FollowWaypoints 액션 클라이언트
        self.action_client_waypoints = ActionClient(self, FollowWaypoints, '/follow_waypoints')

        self._goal_handle = None
        self.init_pose = [-0.169, -0.0438, -0.00143, 1.0]

        # Subscribe to baby_y topic
        self.subscription = self.create_subscription(
            String,
            'baby_y',
            self.baby_y_callback,
            10  # QoS
        )

        self.subscription_danger_pos = self.create_subscription(
            Point,
            'danger_pos',
            self.danger_pos_callback,  # Callback for danger position
            10
        )

        self.set_initial_pose_service_client = self.create_client(
            SetInitialPose,
            '/set_initial_pose'
        )
        while not self.set_initial_pose_service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service /set_initial_pose not available, waiting again...')
        self.set_initial_pose(*self.init_pose)

        # Publisher for cmd_vel to stop the robot
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # Variable to store the dangerous position
        self.status = Point()
        self.is_sending_goals = False  # 목표 전송 상태 관리 플래그
        self.is_goal_completed = False  # 목표가 완료되었는지 확인하는 플래그
        self.previous_baby_y = None  # 이전 baby_y 값을 저장

    def set_initial_pose(self, x, y, z, w):
        req = SetInitialPose.Request()
        req.pose.header.frame_id = 'map'
        req.pose.pose.pose.position = Point(x=x, y=y, z=0.0)
        req.pose.pose.pose.orientation = Quaternion(x=0.0, y=0.0, z=z, w=w)
        req.pose.pose.covariance = [0.1] * 36
        future = self.set_initial_pose_service_client.call_async(req)
        if future.result() is not None:
            self.get_logger().info("Initial pose set successfully")
        else:
            self.get_logger().warning("Failed to set initial pose")

    def send_goal(self, x, y, yaw=0.0):
        # 새로운 PoseStamped 목표 생성
        waypoint = PoseStamped()
        waypoint.header.frame_id = 'map'
        waypoint.header.stamp = self.get_clock().now().to_msg()

        # 웨이포인트의 위치 설정
        waypoint.pose.position.x = x
        waypoint.pose.position.y = y
        waypoint.pose.position.z = 0.0  # 2D 내비게이션을 가정

        # 웨이포인트의 방향 설정 (예시로 회전하지 않도록 설정)
        waypoint.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)

        # NavigateToPose 액션의 목표 메시지 생성
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = waypoint  # 단일 목표 전송

        # 목표를 비동기적으로 전송
        self._send_goal_future = self.action_client_nav.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def send_multiple_goals(self):
        # Define waypoints for FollowWaypoints action
        waypoints = [
            (0.307, -0.0595),      # Corner1
            (0.244, -0.705),    # Corner2
            (-0.826, -0.592),   # Corner3
            (-0.507, -0.0219),  # Corner4
            (-1.51, 0.0282),    # Corner5
            (-1.62, -0.542)     # Corner6
        ]
        
        # 웨이포인트가 이미 전송 중이면 추가적으로 보내지 않음
        if self.is_sending_goals:
            self.get_logger().info("Goals are already being sent. Please wait until they are completed.")
            return
        
        # Create a list of PoseStamped messages for each waypoint
        poses = []
        for x, y in waypoints:
            waypoint = PoseStamped()
            waypoint.header.frame_id = 'map'
            waypoint.header.stamp = self.get_clock().now().to_msg()
            waypoint.pose.position.x = x
            waypoint.pose.position.y = y
            waypoint.pose.position.z = 0.0
            waypoint.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)  # No rotation for now
            poses.append(waypoint)

        # Create the goal message for FollowWaypoints action
        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = poses

        # Set flag to indicate we're sending multiple goals
        self.is_sending_goals = True

        # Wait for the action server to be available
        self.action_client_waypoints.wait_for_server()

        # Send the goal asynchronously
        self._send_goal_future = self.action_client_waypoints.send_goal_async(goal_msg)
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

    def cancel_goal(self):
        # Only cancel if goal is in progress and not completed yet
        if self._goal_handle is not None and not self.is_goal_completed:
            self.get_logger().info('Attempting to cancel the goal...')
            cancel_future = self._goal_handle.cancel_goal_async()
            cancel_future.add_done_callback(self.cancel_done_callback)
        else:
            self.get_logger().info('No active goal to cancel or goal is already completed.')

    def cancel_done_callback(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Goal cancellation accepted.')
        else:
            self.get_logger().info('Goal cancellation failed or no active goal to cancel.')

    def baby_y_callback(self, msg):
        baby_y_value = msg.data  # String 메시지에서 data를 사용
        self.get_logger().info(f'Received baby_y: {baby_y_value}')
        # 이전 값과 다른 경우 목표 취소 및 새 작업 처리
        self.get_logger().info(f'Value changed from {self.previous_baby_y} to {baby_y_value}')
        self.cancel_goal()  # 현재 진행 중인 목표 취소

        # 새로운 baby_y 값에 따른 동작 수행
        if baby_y_value == "10":
            self.send_multiple_goals()  # 다중 목표 전송
        elif baby_y_value == "2":
            self.send_goal(-1.24, -0.02)
            self.is_sending_goals = False
        elif baby_y_value == "1":
            self.send_goal(0.1, -0.629)
            self.is_sending_goals = False
        elif baby_y_value == "3":
            #값이 들어온 경우
            if self.status.x != 0 or self.status.y != 0:
                self.send_goal(self.status.x, self.status.y)
                self.is_sending_goals = False
        else:
            self.cancel_goal()
            self.is_sending_goals = False

        # 이전 값을 현재 값으로 갱신
        self.previous_baby_y = baby_y_value

    def danger_pos_callback(self, msg):
        self.status = msg  # danger_pos 업데이트

    def get_result_callback(self, future):
        result = future.result()
        if result is not None:
            self.get_logger().info(f'Goal completed with result: {result}')
            self.is_goal_completed = True
        else:
            self.get_logger().warning('Goal failed.')

def main(args=None):
    rclpy.init(args=args)
    goal_publisher = GoalPublisher()
    rclpy.spin(goal_publisher)

if __name__ == '__main__':
    main()

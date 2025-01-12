import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from std_msgs.msg import String
from geometry_msgs.msg import Point,Quaternion
from nav2_msgs.srv import SetInitialPose

class GoalPublisher(Node):
    def __init__(self):
        super().__init__('goal_publisher')
        self.action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
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
        self.status = None
    
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
        return future.result()

    def send_goal(self, x, y, yaw=0.0):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()

        # Set goal position
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.position.z = 0.0

        # Wait for the action server to be available
        self.action_client.wait_for_server()
        self.get_logger().info(f'Sending goal to x: {x}, y: {y}...')

        # Send the goal asynchronously
        self._send_goal_future = self.action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected.')
            return

        self.get_logger().info('Goal accepted.')
        self._goal_handle = goal_handle

    def cancel_goal(self):
        if self._goal_handle is not None:
            self.get_logger().info('Attempting to cancel the goal...')
            cancel_future = self._goal_handle.cancel_goal_async()
            cancel_future.add_done_callback(self.cancel_done_callback)
        else:
            self.get_logger().info('No active goal to cancel.')

    def cancel_done_callback(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Goal cancellation accepted. Exiting program...')
        else:
            self.get_logger().info('Goal cancellation failed or no active goal to cancel.')

    def baby_y_callback(self, msg):
        baby_y_value = msg.data
        self.get_logger().info(f'Received baby_y: {baby_y_value}')

        # Check conditions and send goal or stop the robot
        if baby_y_value == "2":
            self.send_goal(-1.24, -0.02)
        elif baby_y_value == "1":
            self.send_goal(0.1, -0.629)
        elif baby_y_value == "3":
            if self.status is not None:
                self.send_goal(self.status.x, self.status.y)
            
        else:
            self.cancel_goal()

    def danger_pos_callback(self, msg):
        self.status = msg  # Store the danger position as status

def main(args=None):
    rclpy.init(args=args)
    node = GoalPublisher()

    rclpy.spin(node)

if __name__ == '__main__':
    main()
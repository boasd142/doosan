import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomSubscriber(Node):
    def __init__(self):
        super().__init__('odom_position_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',  # 토픽 이름 (turtlebot의 odom 토픽)
            self.odom_callback,
            10  # QoS 프로파일
        )
        self.subscription  # 방식을 유지하기 위해 필요합니다.

    def odom_callback(self, msg):
        # Position 정보만 추출
        position = msg.pose.pose.position
        self.get_logger().info(f"Position - x: {position.x}, y: {position.y}, z: {position.z}")

def main(args=None):
    rclpy.init(args=args)

    node = OdomSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
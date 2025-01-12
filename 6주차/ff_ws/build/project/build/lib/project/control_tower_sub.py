import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscribers(Node):
    def __init__(self):
        super().__init__('subscribers_node')  # 노드 이름 설정
        self.get_job_list = self.create_subscription(
            String,  # 메시지 타입
            'job_list',  # 토픽 이름
            self.get_list_callback,  # 콜백 함수
            10  # 큐 사이즈
        )

    def get_list_callback(self, msg):
        # 수신된 메시지를 로그로 출력
        self.get_logger().info(f'{msg.data}')


def main():
    rclpy.init()  # ROS 2 초기화
    node = Subscribers()  # Subscribers 클래스 인스턴스화
    rclpy.spin(node)  # 노드가 종료될 때까지 실행

    node.destroy_node()  # 노드 종료
    rclpy.shutdown()  # ROS 2 종료


if __name__ == '__main__':
    main()

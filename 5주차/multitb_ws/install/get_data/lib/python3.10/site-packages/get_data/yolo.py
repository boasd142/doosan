import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class YoloV8Subscriber(Node):
    def __init__(self):
        super().__init__('yolov8_subscriber')  # 노드 이름 설정
        self.subscription = self.create_subscription(
            String,  # 메시지 타입
            'detected',  # 퍼블리셔가 발행하는 토픽 이름
            self.listener_callback,  # 메시지를 받을 콜백 함수
            10  # 큐 사이즈
        )
        
    def listener_callback(self, msg):
        # 퍼블리셔에서 받은 메시지를 처리하는 부분
        self.get_logger().info(f'Received message: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)  # ROS2 초기화
    yolo_subscriber = YoloV8Subscriber()  # 서브스크라이버 노드 객체 생성

    rclpy.spin(yolo_subscriber)  # 노드가 메시지를 기다리고 처리할 수 있도록 함

    # 종료 시 깨끗하게 정리
    yolo_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
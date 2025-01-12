import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
import numpy as np
import cv2
from cv_bridge import CvBridge

class CameraSubscriber(Node):
    def __init__(self):
        super().__init__('camera_subscriber')

        # 이미지 및 구역 정보를 받을 구독자 생성
        self.create_subscription(
            CompressedImage,
            'turtle_camera',
            self.image_callback,
            10  # 큐 사이즈
        )

        self.create_subscription(
            String,
            'box_condition',
            self.box_condition_callback,
            10  # 큐 사이즈
        )

        # CvBridge 설정
        self.bridge = CvBridge()
        self.detected_zone = None  # 구역 정보 초기화
        self.detected_color = None  # 색상 정보 초기화

    def image_callback(self, msg):
        """이미지 메시지를 수신하고, OpenCV 형식으로 변환 후 화면에 표시"""
        try:
            # 압축된 이미지를 OpenCV 형식으로 변환
            np_arr = np.frombuffer(msg.data, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            if frame is not None:
                # 구역과 색상이 설정되어 있을 경우 이미지 위에 표시
                if self.detected_zone and self.detected_color:
                    text = f"Zone: {self.detected_zone}, Color: {self.detected_color}"
                    cv2.putText(
                        frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (0, 255, 0), 2, cv2.LINE_AA
                    )

                # 이미지를 화면에 표시
                cv2.imshow("Received Image", frame)
                cv2.waitKey(1)  # 1ms 대기 (OpenCV 창을 업데이트하기 위해 필요)
        except Exception as e:
            self.get_logger().error(f"Failed to convert compressed image: {str(e)}")

    def box_condition_callback(self, msg):
        """구역 및 색상 정보 수신"""
        try:
            # 구역 및 색상 정보 파싱
            detected_info = msg.data
            self.get_logger().info(f"Detected info: {detected_info}")

            # "Zone X - Color" 형식의 문자열 파싱
            parts = detected_info.split(" - ")
            if len(parts) == 2:
                self.detected_zone = parts[0].split(" ")[1]  # "Zone X"에서 X 추출
                self.detected_color = parts[1]  # 색상 추출
        except Exception as e:
            self.get_logger().error(f"Failed to parse detected info: {str(e)}")

    def __del__(self):
        # 노드 종료 시 OpenCV 윈도우 종료
        cv2.destroyAllWindows()

def main():
    rclpy.init()  # ROS 2 초기화
    camera_subscriber = CameraSubscriber()  # 구독자 노드 객체 생성
    rclpy.spin(camera_subscriber)  # 노드가 종료될 때까지 실행
    camera_subscriber.destroy_node()  # 노드 종료
    rclpy.shutdown()  # ROS 2 종료

if __name__ == '__main__':
    main()

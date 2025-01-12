import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
from ultralytics import YOLO  # YOLOv8 모델 사용
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')

        # YOLOv8 모델 로드
        self.model = YOLO("best.pt")  # YOLOv8 모델 파일 경로
        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(0)  # 카메라 캡처

        # 퍼블리셔 설정
        self.publisher_image = self.create_publisher(
            Image, 
            'camera_image', 
            10)  # 처리된 프레임 퍼블리셔
        
        self.publisher_detection = self.create_publisher(
            String, 
            'detected', 
            10)  # 감지된 객체 정보 퍼블리셔

        # 타이머 설정 (주기적으로 publish_image 호출)
        self.timer_image = self.create_timer(0.5, self.publish_image)
        self.timer_detection = self.create_timer(0.5, self.publish_detection)

        # 감지된 객체 정보를 저장할 변수
        self.detection_info = ""

    def publish_image(self):
        """카메라 프레임을 캡처, YOLO로 처리 후 퍼블리시."""
        ret, frame = self.capture.read()
        if ret:
            # 프레임 크기 축소 (640x480으로 변경)
            frame = cv2.resize(frame, (640, 480))

            # YOLOv8로 프레임 분석
            results = self.model(frame)

            # 감지된 객체 정보 추출 및 프레임에 바운딩 박스 그리기
            self.detection_info = self.draw_bounding_boxes(frame, results)

            # OpenCV 이미지를 ROS 메시지로 변환 후 퍼블리시
            ros_image = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher_image.publish(ros_image)

    def publish_detection(self):
        """주기적으로 감지된 객체 정보를 퍼블리시."""
        if self.detection_info:
            self.publisher_detection.publish(String(data=self.detection_info))

    def draw_bounding_boxes(self, frame, results):
        """YOLOv8 결과를 기반으로 각 클래스별로 신뢰도가 가장 높은 객체만 표시."""
        # 클래스별로 가장 높은 신뢰도 객체를 추적하기 위한 딕셔너리
        class_best_boxes = {}

        # YOLO 결과에서 바운딩 박스 정보 추출
        for result in results[0].boxes.data.tolist():  
            x1, y1, x2, y2 = map(int, result[:4])  # 바운딩 박스 좌표
            score = result[4]  # 신뢰도 (정확도)
            class_id = int(result[5])  # 클래스 ID
            class_name = self.model.names[class_id]  # 클래스 이름

            # 클래스별로 신뢰도가 가장 높은 객체 찾기
            if class_id not in class_best_boxes:
                class_best_boxes[class_id] = {"score": score, "bbox": (x1, y1, x2, y2), "class_name": class_name}
            else:
                # 기존의 최고 신뢰도보다 더 높은 신뢰도를 가진 객체가 있으면 교체
                if score > class_best_boxes[class_id]["score"]:
                    class_best_boxes[class_id] = {"score": score, "bbox": (x1, y1, x2, y2), "class_name": class_name}

        # 각 클래스별로 가장 신뢰도가 높은 객체만 바운딩 박스를 그리기
        detection_info = ""
        for class_id, best_box in class_best_boxes.items():
            x1, y1, x2, y2 = best_box["bbox"]
            score = best_box["score"]
            class_name = best_box["class_name"]
            
            # 바운딩 박스 그리기
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 초록색 박스
            cv2.putText(frame, f"{class_name} {score:.2f}", 
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 255, 0), 2)  # 클래스 이름과 신뢰도

            # 감지된 객체 정보 저장
            detection_info += f"{class_name} ({score:.2f})\n"

        # 최종 감지된 객체 정보 반환
        return detection_info

def main(args=None):
    rclpy.init(args=args)

    # CameraPublisher 노드 실행
    camera_publisher_node = CameraPublisher()

    # ROS2 스핀
    rclpy.spin(camera_publisher_node)

    # 종료시 리소스 해제
    camera_publisher_node.capture.release()
    camera_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

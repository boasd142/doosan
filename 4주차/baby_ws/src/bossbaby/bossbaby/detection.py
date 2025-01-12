import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
from ultralytics import YOLO  # YOLOv8 모델 사용
from sensor_msgs.msg import CompressedImage  # Image 대신 CompressedImage
from cv_bridge import CvBridge
from geometry_msgs.msg import Point, Twist

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')

        # YOLOv8 모델 로드
        self.model = YOLO("best_monitor.pt")  # YOLOv8 모델 파일 경로
        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(3)  # 카메라 캡처

        # 퍼블리셔 설정 (이제 CompressedImage 타입을 사용)
        self.publisher_image = self.create_publisher(
            CompressedImage,  #CompressedImage
            'camera_image',
            10)  # 처리된 프레임 퍼블리셔

        self.publisher_detection = self.create_publisher(
            String, 
            'detected', 
            10)  # 감지된 객체 정보 퍼블리셔
        
        self.publisher_baby_pos = self.create_publisher(
            Point,
            'baby_pos',
            10
        )
        
        self.publisher_move = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )
        # 감지된 객체 정보를 저장할 변수
        self.detection_info = ""
        self.baby_pose = None

        # 타이머 설정 (주기적으로 publish_image 호출)
        self.timer_image = self.create_timer(0.2, self.publish_image)
        self.timer_detection = self.create_timer(1, self.publish_detection)
        self.timer_baby_pos = self.create_timer(0.2,self.publish_baby_pose)
        self.timer_rotate = self.create_timer(0.1,self.publish_move)

    def publish_move(self):
        if not self.baby_pose:
            return
        
        msg = Twist()
        x = self.baby_pose.x
        y = self.baby_pose.y
        if x > 450:
            msg.angular.z = 0.1
        elif x < 150:
            msg.angular.z = -0.1
        else:
            msg.angular.z = 0.0

        if y > 300:
            msg.linear.x = -0.1
        elif y < 100:
            msg.linear.x = 0.1
        else:
            msg.linear.x = 0.0
        self.publisher_move.publish(msg)
    
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

            # 이미지를 압축하여 퍼블리시
            self.publish_compressed_image(frame)

    def publish_compressed_image(self, frame):
        """이미지를 압축하여 퍼블리시."""
        # JPEG 압축 적용 (품질 50%)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
        _, compressed_frame = cv2.imencode('.jpg', frame, encode_param)

        # 압축된 이미지를 ROS 메시지로 변환
        compressed_image_msg = CompressedImage()
        compressed_image_msg.header.stamp = self.get_clock().now().to_msg()
        compressed_image_msg.header.frame_id = 'camera'
        compressed_image_msg.format = 'jpeg'
        compressed_image_msg.data = compressed_frame.tobytes()

        # 압축된 이미지를 camera_image 토픽으로 퍼블리시
        self.publisher_image.publish(compressed_image_msg)
        

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
            if class_name == 'baby':
                self.baby_pose = Point(
                    x = (x1 + x2) / 2,
                    y = (y1 + y2) / 2,
                    z = 0.0
                )
            # 바운딩 박스 그리기
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 초록색 박스
            cv2.putText(frame, f"{class_name} {score:.2f}", 
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 255, 0), 2)  # 클래스 이름과 신뢰도

            # 감지된 객체 정보 저장
            detection_info += f"{class_name} ({score:.2f})\n"

        # 최종 감지된 객체 정보 반환
        return detection_info
    
    def publish_baby_pose(self):
        if self.baby_pose:
            self.publisher_baby_pos.publish(self.baby_pose)

    def publish_detection(self):
        """주기적으로 감지된 객체 정보를 퍼블리시."""
        if self.detection_info:
            self.publisher_detection.publish(String(data=self.detection_info))

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

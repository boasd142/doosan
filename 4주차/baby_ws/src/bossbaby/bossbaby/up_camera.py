import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
from ultralytics import YOLO  # YOLOv8 모델 사용
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
from geometry_msgs.msg import Point
import numpy as np


class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')
        self.model = YOLO("up_best2.pt")  # YOLOv8 모델 파일 경로
        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(2)  # 카메라 캡처
        self.publisher_image = self.create_publisher(
            CompressedImage, 'up_camera_image', 10)
        self.publisher_danger_area = self.create_publisher(
            String, 'baby_y', 10)
        self.publisher_trans_coor = self.create_publisher(
            Point,
            'danger_pos',
            10
        )

        self.detection_info = ""
        self.baby_pose = None
        self.danger_pose = None
        self.baby_detected = False
        self.danger_detected = False

        self.src_points = np.float32([[27, 238], [604, 199], [56, 428], [522, 408]])
        self.dst_points = np.float32([[-0.388, 0.116], [-0.375, -0.892], [-0.945, -0.0156], [-1.03, -0.71]])
        self.matrix = cv2.getPerspectiveTransform(self.src_points, self.dst_points)

        self.timer_image = self.create_timer(0.2, self.publish_image)
        self.timer_baby_y = self.create_timer(0.2, self.publish_danger_area)
        
    def publish_image(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            results = self.model(frame)
            self.detection_info = self.draw_bounding_boxes(frame, results)
            self.publish_compressed_image(frame)

    def publish_danger_area(self):
        if self.baby_detected:
            if self.danger_detected:
                transformed_baby_pose = self.transform_to_map_coordinates(self.baby_pose)
                transformed_danger_pose = self.transform_to_map_coordinates(self.danger_pose)
                middle_x = (transformed_baby_pose[0] + transformed_danger_pose[0]) / 2
                middle_y = (transformed_baby_pose[1] + transformed_danger_pose[1]) / 2
                middle_point = Point(x=middle_x, y=middle_y)
                self.publisher_danger_area.publish(String(data="3"))
                self.publisher_trans_coor.publish(middle_point)
            else:
                y_value = self.baby_pose.y
                if y_value < 180:
                    status = "1"
                elif y_value > 400:
                    status = "2"
                else:
                    status = "0"
                self.publisher_danger_area.publish(String(data=status))
        else:
            self.get_logger().info("No baby detected.")
            self.publisher_danger_area.publish(String(data="10"))

    def publish_compressed_image(self, frame):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
        _, compressed_frame = cv2.imencode('.jpg', frame, encode_param)
        compressed_image_msg = CompressedImage()
        compressed_image_msg.header.stamp = self.get_clock().now().to_msg()
        compressed_image_msg.format = 'jpeg'
        compressed_image_msg.data = compressed_frame.tobytes()
        self.publisher_image.publish(compressed_image_msg)

    def draw_bounding_boxes(self, frame, results):
        class_best_boxes = {}
        self.baby_detected = False  # 초기화
        self.danger_detected = False  # 초기화

        # 각 클래스에 대해 가장 높은 신뢰도를 가진 바운딩 박스를 찾습니다.
        for result in results[0].boxes.data.tolist():
            x1, y1, x2, y2 = map(int, result[:4])
            score = result[4]
            class_id = int(result[5])
            class_name = self.model.names[class_id]

            # 신뢰도 기준으로 각 클래스에서 가장 높은 신뢰도만 선택
            if class_name not in class_best_boxes or class_best_boxes[class_name]['score'] < score:
                class_best_boxes[class_name] = {
                    "score": score,
                    "bbox": (x1, y1, x2, y2),
                    "class_name": class_name
                }

        # 각 클래스별 최고 신뢰도 바운딩 박스를 기반으로 정보 업데이트
        for class_name, best_box in class_best_boxes.items():
            x1, y1, x2, y2 = best_box["bbox"]
            score = best_box["score"]

            # 바운딩 박스를 그려주고, 해당 클래스명과 신뢰도를 텍스트로 표시
            if class_name == 'baby':
                self.baby_pose = Point(x=(x1 + x2) / 2, y=(y1 + y2) / 2, z=0.0)
                self.baby_detected = True  # baby 감지
                self.get_logger().info(f"Baby detected at {self.baby_pose}")

            elif class_name == 'danger':
                self.danger_pose = Point(x=(x1 + x2) / 2, y=(y1 + y2) / 2, z=0.0)
                self.danger_detected = True  # danger 감지
                self.get_logger().info(f"Danger detected at {self.danger_pose}")

            # 바운딩 박스와 텍스트 그리기
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{class_name} {score:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 감지되지 않았을 경우 초기화
        if not self.baby_detected:
            self.baby_pose = None
        if not self.danger_detected:
            self.danger_pose = None

        # 각 클래스별 최고 신뢰도 정보를 반환
        return " ".join([f"{v['class_name']} ({v['score']:.2f})" for v in class_best_boxes.values()])

    def transform_to_map_coordinates(self, pose):
        src_point = np.array([[[pose.x, pose.y]]], dtype=np.float32)
        transformed_point = cv2.perspectiveTransform(src_point, self.matrix)
        return transformed_point[0][0]


def main(args=None):
    rclpy.init(args=args)
    camera_publisher_node = CameraPublisher()
    rclpy.spin(camera_publisher_node)
    camera_publisher_node.capture.release()
    camera_publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

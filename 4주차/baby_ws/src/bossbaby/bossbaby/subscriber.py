import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import queue
import threading

class DetectionSubscriberNode(Node):
    def __init__(self, img_queue):
        super().__init__('detection_subscriber')
        self.subscription_image = self.create_subscription(
            Image,
            'camera_image',  # ROS 2에서 퍼블리시된 영상 토픽
            self.detection_callback_image,  # 영상 콜백 함수
            10  # 큐 사이즈
        )
        self.bridge = CvBridge()
        self.img_queue = img_queue  # 전달된 큐를 이용해 영상을 Flask 서버로 전달
        self.get_logger().info("DetectionSubscriberNode is running and listening for camera image.")

    def detection_callback_image(self, msg):
        """ROS 2에서 수신한 영상을 OpenCV 형식으로 변환하여 큐에 저장."""
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        self.img_queue.put(frame)  # Flask 서버로 전달하기 위해 큐에 프레임 저장
        self.get_logger().info("Received camera image.")

def main(img_queue):
    rclpy.init()
    detection_subscriber_node = DetectionSubscriberNode(img_queue)
    
    try:
        rclpy.spin(detection_subscriber_node)
    except KeyboardInterrupt:
        pass
    finally:
        detection_subscriber_node.destroy_node()
        rclpy.shutdown()

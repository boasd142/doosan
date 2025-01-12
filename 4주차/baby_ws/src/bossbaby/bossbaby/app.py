import threading
import queue
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Point
from std_msgs.msg import String
from cv_bridge import CvBridge
from flask import Flask, Response, render_template
from ultralytics import YOLO  # YOLOv8 모델 로드

# Flask 애플리케이션 초기화
app = Flask(__name__, template_folder='/home/bok/baby_ws/src/bossbaby/bossbaby/templates')

# 영상 프레임을 저장할 큐
img_queue = queue.Queue(maxsize=10)  # 최대 10개의 영상 프레임을 저장
video_queue = queue.Queue(maxsize=10)  # 두 번째 영상 큐

# YOLOv8 모델 로드 (경로는 모델이 저장된 경로로 설정)
model = YOLO('yolov8n.pt')  # 모델을 로드합니다. yolov8n.pt는 예시입니다.

class ImageSubscriberNode(Node):
    def __init__(self, img_queue):
        super().__init__('image_subscriber')
        
        # 영상 토픽 구독
        self.subscription_image = self.create_subscription(
            CompressedImage,
            'camera_image',  # ROS 2에서 퍼블리시된 영상 토픽
            self.image_callback,  # 영상 콜백 함수
            10  # 큐 사이즈
        )
        
        self.subscription_detection = self.create_subscription(
            String,
            'detected',
            self.detect_callback,
            10
        )

        self.subscription_baby_pose = self.create_subscription(
            Point,
            'baby_pos',
            self.callback_baby_pose,
            10
        )
        self.bridge = CvBridge()
        self.img_queue = img_queue  # 영상 프레임 전달용 큐
    
    def detect_callback(self,msg):
        self.get_logger(f"감지 객체 : {msg.data}")
    
    def callback_baby_pose(self,msg):
        self.get_logger(f"위치 : {msg.x}, {msg.y}")

    def image_callback(self, msg):
        """ROS 메시지를 OpenCV 이미지로 변환 후 큐에 저장"""
        try:
            # CompressedImage의 경우 'compressed_imgmsg_to_cv2' 사용
            frame = self.bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="bgr8")
            if self.img_queue.full():
                self.img_queue.get()  # 큐가 가득 차면 가장 오래된 프레임 제거
            self.img_queue.put(frame)  # 큐에 영상 저장
        except Exception as e:
            self.get_logger().error(f"Error processing image: {e}")

# Flask 웹 서버에서 영상을 스트리밍하는 라우트
@app.route('/video')
def video_feed():
    """웹에서 실시간으로 영상을 스트리밍"""
    def generate():
        while True:
            frame = img_queue.get()  # 큐에서 영상 프레임을 가져옴
            if frame is not None:
                try:
                    # OpenCV 이미지를 JPEG로 인코딩
                    _, encoded_frame = cv2.imencode('.jpg', frame)
                    if not _:
                        raise Exception("Failed to encode image")
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + encoded_frame.tobytes() + b'\r\n')
                except Exception as e:
                    print(f"Error encoding image: {e}")
                    continue  # 이미지 인코딩 실패 시, 계속해서 다음 프레임을 시도
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 두 번째 영상 스트리밍 라우트 (YOLOv8 적용 및 바운딩 박스 그리기)
@app.route('/video2')
def video_feed2():
    """웹에서 두 번째 영상을 스트리밍 (YOLOv8 적용 및 바운딩 박스 표시)"""
    def generate():
        while True:
            frame = video_queue.get()  # 두 번째 영상 큐에서 프레임을 가져옴
            if frame is not None:
                try:
                    # YOLOv8 모델을 사용하여 객체 탐지
                    results = model(frame)  # 모델에 프레임을 입력하여 객체 탐지 수행

                    # 탐지된 객체의 바운딩 박스 및 라벨 정보 그리기
                    annotated_frame = results[0].plot()  # 탐지된 객체에 대한 바운딩 박스 그리기

                    # OpenCV 이미지를 JPEG로 인코딩
                    _, encoded_frame = cv2.imencode('.jpg', annotated_frame)
                    if not _:
                        raise Exception("Failed to encode image")

                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + encoded_frame.tobytes() + b'\r\n')
                except Exception as e:
                    print(f"Error encoding second video: {e}")
                    continue  # 두 번째 영상 인코딩 실패 시, 계속해서 다음 프레임을 시도
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 웹 메인 페이지 제공
@app.route('/')
def index():
    return render_template('monitor.html')

# Flask 서버를 별도의 스레드에서 실행하는 함수
def start_flask():
    """Flask 서버 실행 함수"""
    app.run(debug=False, use_reloader=False, host='0.0.0.0', port=5000)

# ROS 2 노드를 별도의 스레드에서 실행하는 함수
def start_ros_node():
    """ROS 2 노드 실행 함수 - rclpy.spin() 사용"""
    rclpy.init()
    image_subscriber_node = ImageSubscriberNode(img_queue)

    try:
        rclpy.spin(image_subscriber_node)  # 이벤트 루프 실행
    except KeyboardInterrupt:
        pass
    finally:
        image_subscriber_node.destroy_node()  # 실행 후 노드 종료
        rclpy.shutdown()

# 비디오 캡처를 별도로 처리하는 함수 (두 번째 영상 캡처)
def capture_video2():
    cap = cv2.VideoCapture(0)  # 첫 번째 웹캠 장치 (인덱스 0) 사용

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if video_queue.full():
                video_queue.get()  # 큐가 가득 차면 가장 오래된 프레임 제거
            video_queue.put(frame)  # 큐에 영상 저장
        else:
            break
    cap.release()

def main():
    # Flask 서버를 별도의 스레드에서 실행
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True  # 메인 프로그램 종료 시 Flask 서버 스레드도 종료
    flask_thread.start()

    # ROS 2 노드를 별도의 스레드에서 실행
    ros_thread = threading.Thread(target=start_ros_node)
    ros_thread.daemon = True  # 메인 프로그램 종료 시 ROS 2 스레드도 종료
    ros_thread.start()

    # 비디오 캡처 스레드를 별도로 실행 (두 번째 영상 처리)
    video_thread = threading.Thread(target=capture_video2)
    video_thread.daemon = True
    video_thread.start()

    # 메인 스레드는 종료되지 않도록 유지
    ros_thread.join()

if __name__ == "__main__":
    main()

import threading
import queue
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import String
from cv_bridge import CvBridge
from flask import flash,Flask, Response, render_template, request, redirect, url_for, session
from geometry_msgs.msg import Point

# Flask 애플리케이션 초기화
app = Flask(__name__,template_folder='/home/bok/baby_ws/src/bossbaby/bossbaby/templates')



# 영상 프레임을 저장할 큐
img_queue = queue.Queue(maxsize=10)  # 최대 10개의 영상 프레임을 저장
img_queue2 = queue.Queue(maxsize=10)  # 최대 10개의 영상 프레임을 저장


class ImageSubscriberNode(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        
        # AMR 영상 토픽 구독
        self.subscription_image1 = self.create_subscription(
            CompressedImage,
            'amr_camera_image',  # ROS 2에서 퍼블리시된 영상 토픽
            self.image_callback,  # 영상 콜백 함수
            10  # 큐 사이즈
        )
        
        # UP_CAM 영상 토픽 구독
        self.subscription_image2 = self.create_subscription(
            CompressedImage,
            'up_camera_image',  # ROS 2에서 퍼블리시된 영상 토픽
            self.image_callback2,  # 영상 콜백 함수
            10  # 큐 사이즈
        )
        
        self.subscription_area = self.create_subscription(
            String,
            'baby_y',
            self.area_callback,
            10
        )
        self.bridge = CvBridge()
        self.img_queue = img_queue  # 영상 프레임 전달용 큐
        self.img_queue2 = img_queue2
        self.get_logger().info(f"ImageSubscriberNode is running")

        # 객체 감지 결과를 받는 토픽 구독
        self.subscription_detection = self.create_subscription(
            String,
            'detected',
            self.detect_callback,
            10
        )
        
        self.position_baby = self.create_subscription(
            Point,
            'baby_pos',
            self.baby_pos_callback,
            10
        )
    def area_callback(self,msg):
        self.get_logger().info(f"현재 상황 : {msg}")
        
    def baby_pos_callback(self,msg):
        self.get_logger().info(f"포지션: {msg}")

    def image_callback(self, msg):
        """ROS 메시지를 OpenCV 이미지로 변환 후 큐에 저장"""
        # CompressedImage의 경우 'compressed_imgmsg_to_cv2' 사용
        frame = self.bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="bgr8")
        if self.img_queue.full():
            self.img_queue.get()  # 큐가 가득 차면 가장 오래된 프레임 제거
        self.img_queue.put(frame)  # 큐에 영상 저장
        
    def image_callback2(self, msg):
        """ROS 메시지를 OpenCV 이미지로 변환 후 큐에 저장"""
        # CompressedImage의 경우 'compressed_imgmsg_to_cv2' 사용
        frame = self.bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="bgr8")
        if self.img_queue2.full():
            self.img_queue2.get()  # 큐가 가득 차면 가장 오래된 프레임 제거
        self.img_queue2.put(frame)  # 큐에 영상 저장
        

    def detect_callback(self, msg):
        """감지된 객체 정보를 로그에 출력"""
        self.get_logger().info(f"감지 객체: {msg.data}")
    



app.secret_key = 'rokey'
USERNAME = 'admin'
PASSWARD = 'rokey'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USERNAME and password == PASSWARD:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Incorrect username or password', 'error')
            return render_template('login.html')

    return render_template('login.html')

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('monitor.html')

# Flask 웹 서버에서 영상을 스트리밍하는 라우트
@app.route('/video')
def video_feed():
    """웹에서 실시간으로 영상을 스트리밍"""
    def generate():
        while True:
            frame = img_queue.get()  # 큐에서 영상 프레임을 가져옴
            if frame is not None:
                # OpenCV 이미지를 JPEG로 인코딩
                _, encoded_frame = cv2.imencode('.jpg', frame)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + encoded_frame.tobytes() + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
    
@app.route('/video2')
def video_feed2():
    """웹에서 실시간으로 영상을 스트리밍"""
    def generate():
        while True:
            frame = img_queue2.get()  # 큐에서 영상 프레임을 가져옴
            if frame is not None:
                # OpenCV 이미지를 JPEG로 인코딩
                _, encoded_frame = cv2.imencode('.jpg', frame)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + encoded_frame.tobytes() + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/logout',methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Flask 서버를 별도의 스레드에서 실행하는 함수
def start_flask():
    """Flask 서버 실행 함수"""
    app.run(debug=False, use_reloader=False, host='0.0.0.0', port=5000)
    

# ROS 2 노드를 별도의 스레드에서 실행하는 함수
def start_ros_node():
    """ROS 2 노드 실행 함수 - rclpy.spin() 사용"""
    rclpy.init()
    image_subscriber_node = ImageSubscriberNode()

    try:
        rclpy.spin(image_subscriber_node)  # 이벤트 루프 실행
    except KeyboardInterrupt:
        pass
    finally:
        image_subscriber_node.destroy_node()  # 실행 후 노드 종료
        rclpy.shutdown()

def main():
    # Flask 서버를 별도의 스레드에서 실행
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True  # 메인 프로그램 종료 시 Flask 서버 스레드도 종료
    flask_thread.start()

    # ROS 2 노드를 별도의 스레드에서 실행
    ros_thread = threading.Thread(target=start_ros_node)
    ros_thread.daemon = True  # 메인 프로그램 종료 시 ROS 2 스레드도 종료
    ros_thread.start()

    # 메인 스레드는 종료되지 않도록 유지
    ros_thread.join()
    
if __name__ == "__main__":
    main()

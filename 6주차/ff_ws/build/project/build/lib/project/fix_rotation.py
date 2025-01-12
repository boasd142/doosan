import rclpy
import threading
import cv2, math
import numpy as np
import cv2.aruco as aruco
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32, Header
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge

# 로봇팔 거리계산
r1 = 130
r2 = 124
r3 = 126
th1_offset = - math.atan2(0.024, 0.128)
th2_offset = - 0.5 * math.pi - th1_offset

def solv2(r1, r2, r3):
    d1 = (r3**2 - r2**2 + r1**2) / (2 * r3)
    d2 = (r3**2 + r2**2 - r1**2) / (2 * r3)
    s1 = math.acos(d1 / r1)
    s2 = math.acos(d2 / r2)
    return s1, s2

def solv_robot_arm2(x, y, z, r1, r2, r3):
    Rt = math.sqrt(x**2 + y**2 + z**2)
    Rxy = math.sqrt(x**2 + y**2)
    St = math.asin(z / Rt)
    Sxy = math.atan2(y, x)
    s1, s2 = solv2(r1, r2, Rt)

    sr1 = math.pi / 2 - (s1 + St)
    sr2 = s1 + s2
    sr2_ = sr1 + sr2
    sr3 = math.pi - sr2_

    J0 = (0, 0, 0)
    J1 = (J0[0] + r1 * math.sin(sr1) * math.cos(Sxy),
          J0[1] + r1 * math.sin(sr1) * math.sin(Sxy),
          J0[2] + r1 * math.cos(sr1))
    J2 = (J1[0] + r2 * math.sin(sr1 + sr2) * math.cos(Sxy),
          J1[1] + r2 * math.sin(sr1 + sr2) * math.sin(Sxy),
          J1[2] + r2 * math.cos(sr1 + sr2))
    J3 = (J2[0] + r3 * math.sin(sr1 + sr2 + sr3) * math.cos(Sxy),
          J2[1] + r3 * math.sin(sr1 + sr2 + sr3) * math.sin(Sxy),
          J2[2] + r3 * math.cos(sr1 + sr2 + sr3))

    return J0, J1, J2, J3, Sxy, sr1, sr2, sr3, St, Rt

joint_angle_delta = 0.1  # radian

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_node')

        self.joint_pub = self.create_publisher(
             JointTrajectory, 
             '/arm_controller/joint_trajectory',
             10
        )
       
        # 작업 시작 서브스크라이버
        self.start_subscriber = self.create_subscription(
            Int32,
            'start',
            self.start_callback,
            10
        )
        
        # 비상정지 서브스크라이버
        self.stop_subscriber = self.create_subscription(
            Int32,
            'stop',
            self.stop_callback,
            10
        )
       
        # cmd_vel 퍼블리셔
        self.move_publisher = self.create_publisher(
            Twist,
            'cmd_vel',
            10
        )
        
        # 작업 위치 도착시 퍼블리셔
        self.arrive_publisher = self.create_publisher(
            Int32,
            'arrive',
            10
        )
        
        # 월드뷰 캠 퍼블리셔
        self.publisher_image = self.create_publisher(
            CompressedImage,
            'up_camera',
            10  # 큐 사이즈
        )
    
        # 비상 정지 변수
        self.stop_check = 0
    
        # 다음 단계 진입 확인 변수
        self.step = -1
        
        # 아르코마커 벡터
        self.id = None
        self.rvec = None
        self.tvec = None

        self.rotation_vectors = {
            60: None,
            62: None,
            63: None,
            64: None,
            65: None,
            66: None,
        }

        self.translation_vectors = {
            60: None,
            62: None,
            63: None,
            64: None,
            65: None,
            66: None,
        }

        # 로봇 기준 y좌표 차이(앞뒤로 움직임, 1 당 1m)
        self.y_60location = 0
        self.y_62location = 0
        self.y_63location = 0
        self.y_64location = 0
        self.y_65location = 0
        
        # 비틀림 각도 저장 변수
        self.angle = 0

        # 첫 프레임 저장
        self.read_frame()

        # 아르코 마커 y축 상대 위치 계산
        self.location_cal()

        # 카메라 캡처 설정
        self.capture = cv2.VideoCapture(2)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        if not self.capture.isOpened():
            self.get_logger().error("캠을 열 수 없습니다.")
            return

        # CvBridge 설정
        self.bridge = CvBridge()

        self.get_logger().info("월드뷰 이미지 퍼블리시 준비")
        # 월드뷰 이미지 퍼블리시
        self.timer = self.create_timer(0.1, self.publish_image)
        
        #로봇팔 시작자세
        self.trajectory_msg = JointTrajectory()
        J0, J1, J2, J3, Sxy, sr1, sr2, sr3, St, Rt = solv_robot_arm2(100, 0, 100, r1, r2, r3)
        self.trajectory_msg.header = Header()
        self.trajectory_msg.header.frame_id = ''
        self.trajectory_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']
        
        point = JointTrajectoryPoint()
        point.positions = [Sxy, sr1 + th1_offset, sr2 + th2_offset, sr3]
        point.velocities = [0.0] * 4
        point.time_from_start.sec = 1
        point.time_from_start.nanosec = 5000
        self.trajectory_msg.points = [point]

        self.trajectory_msg.points[0].positions[0] = 0.0
        self.trajectory_msg.points[0].positions[1] = -0.845402829343338
        self.trajectory_msg.points[0].positions[2] = 0.47597600165170617
        self.trajectory_msg.points[0].positions[3] = 1.4402231544865285            
        self.joint_pub.publish(self.trajectory_msg)

        # 터틀봇 작동
        self.move()


    def publish_image(self):
        self.get_logger().info("월드뷰 이미지 퍼블리시 시작")
        
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))  # 이미지 크기 조정

            # 압축된 이미지로 퍼블리시
            compressed_image_msg = CompressedImage()
            compressed_image_msg.header.stamp = self.get_clock().now().to_msg()
            compressed_image_msg.format = 'jpeg'
            
            # 이미지 압축 품질을 50으로 설정
            _, img_encoded = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])  # 50은 압축 품질
            
            compressed_image_msg.data = np.array(img_encoded).tobytes()

            self.publisher_image.publish(compressed_image_msg)


    def stop_callback(self, msg):
        temp = msg.data
        if temp == 1:
            self.stop_check += 1

    def start_callback(self, msg):
        temp = msg.data
        if temp == 1:
            self.step += 1


    def get_angle(self):
        self.get_logger().info("실시간 아르코마커 저장 시도")

        # 카메라 매트릭스와 왜곡 계수 (캘리브레이션 후 얻은 값)
        cameraMatrix = np.array([[1.38992675e+03, 0.00000000e+00, 1.09573766e+03],
                                 [0.00000000e+00, 1.39126023e+03, 7.02526462e+02],
                                 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

        distCoeffs = np.array([0.13879985, -0.35371541, -0.00368127, -0.00311165, 0.22808276])

        # 아루코 마커 감지
        cap = cv2.VideoCapture(2)

        if not cap.isOpened():
            print("캠을 열 수 없습니다.")
            exit()
            
        while True:
            ret, frame = cap.read()

            if not ret:
                print("프레임을 읽을 수 없습니다.")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_100)
            parameters = aruco.DetectorParameters_create()
            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

            # 마커의 위치와 회전 추정
            markerLength = 0.1  # 마커의 실제 크기 (미터 단위)
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, markerLength, cameraMatrix, distCoeffs)  

            # 벡터 값 저장
            self.id = ids
            self.rvec = rvec
            self.tvec = tvec

            # 값 출력
            # self.get_logger().info(f"Marker ID: {self.id}")
            # self.get_logger().info(f"Rotation Vector: {self.rvec}")
            # self.get_logger().info(f"Translation Vector: {self.tvec}")

            # 주어진 회전 벡터와 이동 벡터
            for i, id_value in enumerate(self.id):
                id_num = id_value[0]  # id_value가 리스트로 감싸져 있으므로 첫 번째 값 추출
                self.rotation_vectors[id_num] = np.array(self.rvec[i][0])  # 해당 rvec 값을 np.array 형식으로 저장

            self.angle = self.rotation_vectors[66][1]
            msg = Twist()
            
            if self.angle < -0.05:  # 오른쪽 회전
                msg.angular.z = -0.1
                #self.get_logger().info(f"회전 보정: {self.angle}오른쪽 회전")
                
            elif self.angle > 0.05: # 왼쪽 회전
                msg.angular.z = 0.1
                #self.get_logger().info(f"회전 보정: {self.angle}왼쪽 회전")
                
            else:
                msg.angular.z = 0.0
                #self.get_logger().info(f"회전 보정 완료{self.angle}")
            
            self.move_publisher.publish(msg)
                
        

    def read_frame(self):
        if self.step == -1:
            self.get_logger().info("첫 아르코마커 저장 시도")

            # 카메라 매트릭스와 왜곡 계수 (캘리브레이션 후 얻은 값)
            cameraMatrix = np.array([[1.38992675e+03, 0.00000000e+00, 1.09573766e+03],
                                    [0.00000000e+00, 1.39126023e+03, 7.02526462e+02],
                                    [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

            distCoeffs = np.array([0.13879985, -0.35371541, -0.00368127, -0.00311165, 0.22808276])

            # 아루코 마커 감지
            cap = cv2.VideoCapture(2)

            if not cap.isOpened():
                print("캠을 열 수 없습니다.")
                exit()
            
            ret, frame = cap.read()

            if not ret:
                print("프레임을 읽을 수 없습니다.")


            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_100)
            parameters = aruco.DetectorParameters_create()
            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

            # 마커의 위치와 회전 추정
            markerLength = 0.1  # 마커의 실제 크기 (미터 단위)
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, markerLength, cameraMatrix, distCoeffs)  

            # 벡터 값 저장
            self.id = ids
            self.rvec = rvec
            self.tvec = tvec

            # 값 출력
            self.get_logger().info(f"Marker ID: {self.id}")
            self.get_logger().info(f"Rotation Vector: {self.rvec}")
            self.get_logger().info(f"Translation Vector: {self.tvec}")
            
            # 주어진 회전 벡터와 이동 벡터
            for i, id_value in enumerate(self.id):
                id_num = id_value[0]  # id_value가 리스트로 감싸져 있으므로 첫 번째 값 추출
                self.rotation_vectors[id_num] = np.array(self.rvec[i][0])  # 해당 rvec 값을 np.array 형식으로 저장

            for i, id_value in enumerate(self.id):
                id_num = id_value[0]  # id_value가 리스트로 감싸져 있으므로 첫 번째 값 추출
                self.translation_vectors[id_num] = np.array(self.tvec[i][0])  # 해당 rvec 값을 np.array 형식으로 저장
        else:
            self.get_logger().info("실시간 자세보정 시작")
        
            self.get_angle()
                
        
    def location_cal(self):
        self.get_logger().info("상대위치 계산")

        # 66번 마커의 회전 벡터를 회전 행렬로 변환
        R_66, _ = cv2.Rodrigues(self.rotation_vectors[66])

        # 66번 마커를 기준으로 상대적 좌표 계산
        relative_position_60_from_66 = R_66.T @ (self.translation_vectors[60] - self.translation_vectors[66])
        relative_position_62_from_66 = R_66.T @ (self.translation_vectors[62] - self.translation_vectors[66])
        relative_position_63_from_66 = R_66.T @ (self.translation_vectors[63] - self.translation_vectors[66])
        relative_position_64_from_66 = R_66.T @ (self.translation_vectors[64] - self.translation_vectors[66])
        relative_position_65_from_66 = R_66.T @ (self.translation_vectors[65] - self.translation_vectors[66])

        # 매니퓰레이터 위치 보정
        self.y_60location = relative_position_60_from_66[1] - 0.14
        self.y_62location = relative_position_62_from_66[1] - 0.15
        self.y_63location = relative_position_63_from_66[1] - 0.15
        self.y_64location = relative_position_64_from_66[1] - 0.15

        # 작업 테이블 보정 + 로봇 크기 보정
        self.y_65location = relative_position_65_from_66[1] - 0.24 - 0.2
        
        self.step += 1


    def stop(self):
        self.get_logger().info("비상 정지 대기")
        while self.stop_check == 0:
            rclpy.spin_once(self)
        rclpy.shutdown()


    def move(self):
        # 스레드로 실시간 프레임 읽고 자세 보정
        self.vector_thread = threading.Thread(target=self.read_frame)
        self.vector_thread.start()

        # 0단계
        while self.step == 0:
            self.get_logger().info("0. 대기중")
            rclpy.spin_once(self)
        
        # 비상정지 스레드
        self.stop_thread = threading.Thread(target=self.stop)
        self.stop_thread.start()

        # 1단계
        self.sleep_thread = threading.Thread(target=self.sleep_task, args=(self.y_65location * 10,))
        self.sleep_thread.start()            

        while self.step == 1:
            self.get_logger().info("1. 작업물 접근")
            self.move_forward()

        # 2단계
        arrive_msg = Int32()
        arrive_msg.data = 1
        self.arrive_publisher.publish(arrive_msg)
        
        self.sleep_temp_thread = threading.Thread(target=self.sleep_task, args=(80,))
        self.sleep_temp_thread.start()         
        
        while self.step == 2:
            self.get_logger().info("2. 상자 컨베이어벨트 옮기기")

        # 3단계
        self.sleep_thread = threading.Thread(target=self.sleep_task, args=((self.y_65location - self.y_60location) * 10,))
        self.sleep_thread.start()

        while self.step == 3:
            self.get_logger().info("3. 바구니 이동")
            self.move_backward()

        # 4단계
        arrive_msg.data = 2
        self.arrive_publisher.publish(arrive_msg)
        
        self.sleep_thread = threading.Thread(target=self.sleep_task, args=(17,))
        self.sleep_thread.start()   
            
        while self.step == 4:
            self.get_logger().info("4. 상자 확인 및 잡기")

        # 5단계
        # 목표지점 62
        self.sleep_thread = threading.Thread(target=self.sleep_task, args=((self.y_62location - self.y_60location) * 10,))
        # 목표지점 63
        #self.sleep_thread = threading.Thread(target=self.sleep_task, args=((self.y_63location - self.y_60location) * 10,))
        # 목표지점 64
        #self.sleep_thread = threading.Thread(target=self.sleep_task, args=((self.y_64location - self.y_60location) * 10,))
        self.sleep_thread.start()

        while self.step == 5:
            self.get_logger().info("5. 목표 지점 이동")
            self.move_forward()

        # 6단계
        arrive_msg.data = 3
        self.arrive_publisher.publish(arrive_msg)
        
        self.sleep_thread = threading.Thread(target=self.sleep_task, args=(5,))
        self.sleep_thread.start()   

        while self.step == 6:
            self.get_logger().info("6. 목표지점 바구니 옮기기")
            
        self.get_logger().info("<< 작업 완료 >>")


    def sleep_task(self, wait_time):
        self.get_logger().info(f"Sleeping for {wait_time}sec in a separate thread...")
        threading.Event().wait(wait_time)

        # 다음 단계 진입 확인 변수
        self.step += 1 


    # 0.1은 1초에 0.1m 이동
    def move_forward(self):
        msg = Twist()
        msg.linear.x = -0.1
        
        if self.angle < -0.05:  # 오른쪽 회전
                msg.angular.z = -0.1
                self.get_logger().info("회전 보정: 오른쪽 회전")
                
        elif self.angle > 0.05: # 왼쪽 회전
            msg.angular.z = 0.1
            self.get_logger().info("회전 보정: 왼쪽 회전")
            
        else:
            msg.angular.z = 0.0
            self.get_logger().info("회전 보정 완료")
        
        self.move_publisher.publish(msg)


    # 0.1은 1초에 0.1m 이동
    def move_backward(self):
        msg = Twist()
        msg.linear.x = 0.1
        
        if self.angle < -0.05:  # 오른쪽 회전
            msg.angular.z = -0.05
            self.get_logger().info("회전 보정: 오른쪽 회전")
                
        elif self.angle > 0.05: # 왼쪽 회전
            msg.angular.z = 0.05
            self.get_logger().info("회전 보정: 왼쪽 회전")
            
        else:
            msg.angular.z = 0.0
            self.get_logger().info("회전 보정 완료")
        
        self.move_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    move_node = MoveRobot()
    rclpy.spin(move_node)

    move_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
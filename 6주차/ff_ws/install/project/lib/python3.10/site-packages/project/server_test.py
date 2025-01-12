import os
import serial, serial.tools.list_ports
import threading
import getkey
import re
import cv2
import rclpy
import numpy as np
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from rclpy.timer import Timer
from type.srv import StartTime  # StartTime 서비스 정의

save_directory = "/home/bok/data_img"

class ControlTowerServer(Node):
    def __init__(self):
        super().__init__('control_tower_server')
        self.image_count = 1
        self.arduino_port = '/dev/ttyACM0'
        self.baudrate = 115200
        self.arduino = None

        # rclpy.Timer를 사용하여 주기적으로 check_arduino 호출
        self.arduino_timer = self.create_timer(1.0, self.check_arduino)  # 1초마다 호출
        self.create_service(StartTime, 'job_list', self.job_service_callback)
        self.constart_srv = self.create_service(StartTime, 'constart_button', self.handle_constart_button)  # 서비스 생성
        self.constop_srv = self.create_service(StartTime, 'constop_button', self.handle_constop_button)
        self.data_srv = self.create_service(StartTime, 'data_button', self.handle_data_button)

        self.image_subscriber = None
        self.show_image = False
        self.red_count = 0
        self.blue_count = 0

    def check_arduino(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        try:
            if self.arduino is None or not self.arduino.isOpen():
                # 연결이 없거나, 연결이 끊어진 경우
                print("아두이노 연결 시도 중...")
                self.arduino = serial.Serial(self.arduino_port, self.baudrate, timeout=1)
                print('연결 완료!')

            # 연결이 정상인 경우
            if self.arduino.isOpen():
                self.connection = 1

            if '/dev/ttyACM0' not in ports:
                # 연결 실패 처리
                self.send_email("sorkaksema@naver.com", "XPLW2BFKH76J", "sorkaksema@naver.com", "아두이노 연결 실패", "아두이노 연결 실패")
                print('연결 실패')
                self.arduino = None
        except Exception as e:
            print(f'오류 사항 : {e}')

    def job_service_callback(self, request, response):
        # 받은 요청 값 출력
        self.get_logger().info(f"Received job: {request.job_list}")
        job_list = request.job_list
        red_match = re.search(r'RED:\s*(\d+)', job_list)
        blue_match = re.search(r'BLUE:\s*(\d+)', job_list)
        # 결과 처리 (예시로 start_value가 1일 때 작업 성공, 아니면 실패)
        if red_match:
            self.red_count = int(red_match.group(1))
        else:
            self.red_count = 0
        if blue_match:
            self.blue_count = int(blue_match.group(1))
        else:
            self.blue_count = 0
        if len(request.job_list) >= 10:
            response.status = "SUCCESS"  # 성공 상태
            self.arduino.write('1000'.encode()+b'\n')  # '1000'을 바이트 형식으로 전송       
            print('data sended')
        else:
            response.status = "FAILURE"  # 실패 상태
        return response

    def handle_constart_button(self, request, response):
        if request.constatus == 1:
            request.datastatus = 0
            self.get_logger().info(f"Coveyor handle start: {request.constatus}")
            response.conv = "Conveyor handle started"
            self.arduino_handle(request)
        else:
            response.conv = "conv didn't start"
            self.get_logger().info('con_status is not True')
        return response  # 전체 response 객체를 반환
    
    def arduino_handle(self,request):
        while(rclpy.ok()):
            key_value = getkey.getkey()
            
            if key_value == 'z':
                self.arduino.write('10'.encode()+b'\n')
            elif key_value == 'q':
                request.constatus = 0
                self.get_logger().info(f'stopped : {request.constatus}')
                break

    def handle_constop_button(self, request, response):
        if request.constatus == 0:
            request.datastatus = 0
            self.get_logger().info(f"Conveyor handle stop: {request.constatus}")
            response.conv = "Conveyor handle stopped"
        else:
            response.conv = "conv didn't stop"
            self.get_logger().info('con_status is not False')
        
        return response  # 전체 response 객체를 반환



    def handle_data_button(self, request, response):
        if request.datastatus == 1:
            request.constatus = 0
            self.get_logger().info(f"Data status : {request.datastatus}")

            if not self.image_subscriber:
                self.image_subscriber = self.create_subscription(
                    CompressedImage, 
                    'turtle_camera', 
                    self.image_callback, 
                    10
                )
                self.show_image = True
                self.get_logger().info("Subscribed to /camera/compressed")

            response.data = "SUCCESS"
        else:
            self.show_image = False
            response.data = "FAILURE"
        
        return response  # 전체 response 객체를 반환

    def image_callback(self, msg):
        if self.show_image:
            np_arr = np.frombuffer(msg.data, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            if frame is not None:
                cv2.imshow("Compressed Image", frame)
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord('x'):  # 'x'를 눌러 이미지를 멈춤
                    self.show_image = False
                    cv2.destroyAllWindows()
                    self.get_logger().info("Stopped showing images.")
                    self.image_subscriber = None

                elif key == ord('z'):  # 'z'를 눌러 이미지를 저장
                    if not os.path.exists(save_directory):
                        os.makedirs(save_directory)  # 저장 디렉터리 생성
                    image_path = os.path.join(save_directory, f"image_{self.image_count}.jpg")
                    self.image_count+=1
                    cv2.imwrite(image_path, frame)
                    self.get_logger().info(f"Image saved: {image_path}")
                    
                    
def main(args=None):
    rclpy.init(args=args)
    server = ControlTowerServer()
    rclpy.spin(server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

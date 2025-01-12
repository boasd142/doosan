import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool  # SetBool 서비스 임포트
import cv2
import os

# 저장 디렉토리 설정
save_directory = "/home/rokey/data_img"

class ButtonServer(Node):
    def __init__(self):
        super().__init__('button_server')  # 노드 이름 설정
        self.constart_srv = self.create_service(SetBool, 'constart_button', self.handle_constart_button)  # 서비스 생성
        self.constop_srv = self.create_service(SetBool, 'constop_button', self.handle_constop_button)
        self.data_srv = self.create_service(SetBool, 'data_button', self.handle_data_button)
        
        # "작동중" 메시지를 주기적으로 출력하기 위한 타이머
        self.timer = None
        self.is_running = False  # 컨베이어가 작동 중인지 상태 변수        
        
    def handle_constart_button(self, request, response):
        if request.data:
            response.success = True
            response.message = "컨베이어 벨트가 작동합니다."
            self.get_logger().info("컨베이어 벨트가 작동합니다.")
            if not self.is_running:
                # "작동중" 토픽을 1초마다 출력하는 타이머 시작
                self.timer = self.create_timer(1.0, self.publish_working_status)
                self.is_running = True
        else:
            response.success = False
            response.message = "컨베이어 시작 버튼이 클릭되지 않았습니다."
            self.get_logger().info("컨베이어 시작 버튼이 클릭되지 않았습니다.")
        return response
        
    def handle_constop_button(self, request, response):
        if request.data:
            response.success = True
            response.message = "컨베이어 벨트가 정지합니다."
            self.get_logger().info("컨베이어 벨트가 정지합니다.")
            if self.is_running:
                # 타이머를 멈추고 "작동중" 메시지 출력을 중지
                self.timer.cancel()
                self.is_running = False            
        else:
            response.success = False
            response.message = "컨베이어 정지 버튼이 클릭되지 않았습니다."
            self.get_logger().info("컨베이어 정지 버튼이 클릭되지 않았습니다.")
        return response
        
    def handle_data_button(self, request, response):
        if request.data:
            response.success = True
            response.message = "데이터 수집을 시작합니다."
            self.get_logger().info("데이터 수집을 시작합니다.")
            self.capture_image()
            self.get_logger().info("데이터 수집이 완료되었습니다.")
        else:
            response.success = False
            response.message = "데이터 수집 버튼이 클릭되지 않았습니다."
            self.get_logger().info("데이터 수집 버튼이 클릭되지 않았습니다.")
        return response
        
    def capture_image(self):
        # 디렉토리 생성
        os.makedirs(save_directory, exist_ok=True)

        file_prefix = input("Enter a file prefix to use : ")
        file_prefix = f'{file_prefix}_'
        print(file_prefix)

        image_count = 0
        # cap = cv2.VideoCapture(0)   #PC Camera
        cap = cv2.VideoCapture(0)   #USB Camera

        while image_count < 300:  # 최대 300장까지만 캡처
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow("Webcam", frame)

            key = cv2.waitKey(1)

            if key == ord('q'):  # 'q' 키를 눌러 강제 종료 가능
                print("캡처가 사용자에 의해 중단되었습니다.")
                break
            else:
                file_name = f'{save_directory}/{file_prefix}img_{image_count}.jpg'
                cv2.imwrite(file_name, frame)
                print(f"Image saved. name:{file_name}")
            image_count += 1
    
        print(f"총 {image_count}장의 이미지가 저장되었습니다.")
        cap.release()
        cv2.destroyAllWindows()
    
        # "작동중" 메시지를 주기적으로 출력하는 함수
    def publish_working_status(self):
        if self.is_running:
            print(self.is_running)
            self.get_logger().info("작동중")
        else:
            self.get_logger().info("작동중 메시지가 종료되었습니다.")


def main(args=None):
    rclpy.init(args=args)
    button_server = ButtonServer()  # 서버 객체 생성
    rclpy.spin(button_server)  # 서버 실행 대기
    rclpy.shutdown()

if __name__ == '__main__':
    main()

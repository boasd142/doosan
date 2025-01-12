import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import tkinter as tk
from threading import Thread

class RestaurantOrderSubscriber(Node):
    def __init__(self):
        super().__init__('restaurant_order_subscriber')
        self.subscription = self.create_subscription(String, 'order_topic', self.order_callback, 10)

        # GUI 초기화
        self.root = tk.Tk()
        self.root.title("테이블 주문 현황")

        # 테이블별 주문 내역을 표시할 9개의 칸 생성
        self.order_labels = {}
        for i in range(3):
            for j in range(3):
                table_num = i * 3 + j + 1  # 테이블 번호 1~9
                frame = tk.Frame(self.root, relief="solid", bd=1, width=500, height=500)
                frame.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

                # 테이블 번호와 주문 내역을 표시할 라벨
                table_label = tk.Label(frame, text=f"테이블 {table_num}", font=("Arial", 12, "bold"))
                table_label.pack(anchor="n")
                order_label = tk.Label(frame, text="주문 없음", font=("Arial", 10), justify="left")
                order_label.pack(anchor="w")
                self.order_labels[table_num] = order_label  # 각 테이블 번호에 해당하는 라벨 저장

        # 행 및 열 비율 조정
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        # GUI 종료 설정
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ROS 2 spin을 별도의 스레드에서 실행
        self.spin_thread = Thread(target=self.spin_ros)
        self.spin_thread.start()

        # GUI 메인 루프 실행
        self.root.mainloop()

    def order_callback(self, msg):
        """ROS 2 메시지 콜백 함수 - 테이블 번호에 따라 해당 라벨에 주문 내역 표시"""
        data = msg.data.split('\t')
        if len(data) == 2:
            try:
                table_num = int(data[0])  # 테이블 번호 추출
                order_summary = data[1]   # 주문 내용 추출

                if table_num in self.order_labels:
                    # Tkinter 메인 스레드에서 GUI 업데이트
                    self.root.after(0, self.update_order_label, table_num, order_summary)
                else:
                    self.get_logger().info(f"알 수 없는 테이블 번호: {table_num}")
            except ValueError:
                self.get_logger().info("잘못된 메시지 형식")

    def update_order_label(self, table_num, order_summary):
        """주문 내역을 해당 테이블에 업데이트"""
        self.order_labels[table_num].config(text=order_summary)  # 해당 테이블 칸에 주문 내용 표시

    def spin_ros(self):
        """ROS 2 spin을 별도의 스레드에서 실행"""
        rclpy.spin(self)

    def on_closing(self):
        """창 닫기 시 ROS 정리"""
        rclpy.shutdown()
        self.root.quit()  # Tkinter 종료

def main():
    rclpy.init()
    RestaurantOrderSubscriber()

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from tkinter import messagebox, Tk, Button, Listbox, Frame, Label
from order_msgs.srv import Order  # 주문 서비스 임포트
import threading  # 스레드 모듈 임포트
from PIL import Image, ImageTk  # 이미지 처리 라이브러리 임포트
import os  # 경로 관련 라이브러리 임포트

class MenuGUI(Node):
    def __init__(self, table_num):
        super().__init__(f'menu_gui_{table_num}')

        # ROS 2 클라이언트 초기화 (각 테이블마다 독립적인 클라이언트 생성)
        self.cli = self.create_client(Order, 'order')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('서비스가 아직 준비되지 않았습니다...')

        self.table_num = table_num  # 테이블 번호
        self.root = Tk()
        self.root.title(f"메뉴 화면 - 테이블 {self.table_num}")

        # 메뉴 항목 정의
        self.menu_items = {
            "아이스 아메리카노": 2500,
            "아이스 라떼": 2500,
            "감자한알": 1000,
            "뽀로로 케이크": 13000
        }

        # 절대경로로 이미지 파일 경로 설정
        base_path = "/home/bok/project_ws/src/turtlebot/turtlebot/images"  # 이미지 파일이 위치한 절대경로
        self.menu_images = {
            "아이스 아메리카노": os.path.join(base_path, "ame1.jpg"),
            "아이스 라떼": os.path.join(base_path, "ra1.jpg"),
            "감자한알": os.path.join(base_path, "pota1.jpg"),
            "뽀로로 케이크": os.path.join(base_path, "pororo1.jpg")
        }

        # 주문 내역과 총 가격 초기화
        self.order = {}
        self.total_price = 0.0

        # 메뉴 화면 설정
        row = 1
        Label(self.root, text="메뉴", font=("Arial", 16)).grid(row=0, column=0, columnspan=2)

        # 메뉴 항목 버튼 및 이미지 추가
        for index, (item, price) in enumerate(self.menu_items.items()):
            # 이미지 추가
            row_offset = (index // 2) * 2  # 이미지와 버튼을 같은 행에 배치하기 위해 계산
            self.add_image(item, index, row + row_offset)
            
            # 메뉴 항목 버튼 배치 (이미지 아래에 버튼 배치)
            Button(self.root, text=f"{item} - {price}원", command=lambda item=item: self.add_to_order(item)).grid(row=row + row_offset + 1, column=index % 2, padx=5, pady=(0, 10))

        # 주문 내역과 가격 표시
        order_frame = Frame(self.root)
        order_frame.grid(row=1, column=2, rowspan=5, columnspan=2, sticky="ns", padx=15, pady=5)

        self.order_listbox = Listbox(order_frame, width=30)
        self.order_listbox.pack(side="left", fill="both", expand=True)

        # 주문 버튼
        order_button = Button(self.root, text="주문하기", command=self.place_order, width=4, height=1)
        order_button.grid(row=row + 9, column=3, columnspan=1, padx=5, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_image(self, item, index, row):
        """이미지 추가 함수"""
        # 이미지 경로 가져오기
        image_path = self.menu_images.get(item)

        if image_path:
            try:
                # 이미지 열기
                image = Image.open(image_path)
                image = image.resize((100, 100), Image.Resampling.LANCZOS)  # 크기 조정 (필요시)
                photo = ImageTk.PhotoImage(image)

                # 이미지 삽입
                label = Label(self.root, image=photo)
                label.image = photo  # 이미지를 메모리에 유지해야 함
                label.grid(row=row, column=index % 2, padx=5, pady=5)
            except Exception as e:
                print(f"이미지 로딩 오류: {e}")

    def place_order(self):
        """주문을 서비스로 발행"""
        if not self.order:
            messagebox.showwarning("주문 경고", "주문 항목이 없습니다.")
            return

        # 주문이 완료된 후 한 번만 완료 창이 뜨도록 설정
        if hasattr(self, 'order_placed') and self.order_placed:
            messagebox.showinfo("이미 주문됨", "주문이 이미 완료되었습니다.")
            return

        self.order_placed = True  # 주문 완료 플래그 설정

        orders_to_send = []

        for item, quantity in self.order.items():
            price = self.menu_items[item]
            order_request = Order.Request()
            order_request.table_num = str(self.table_num)  # 각 테이블 번호 사용
            order_request.item = item
            order_request.quantity = quantity
            order_request.price = price
            orders_to_send.append(order_request)

        all_orders_successful = True

        # 한 번에 여러 주문을 전송하는 부분
        for order_request in orders_to_send:
            future = self.cli.call_async(order_request)
            rclpy.spin_until_future_complete(self, future)

            response = future.result()
            if response.success:
                self.get_logger().info(f"주문 완료: {response.message}")
            else:
                self.get_logger().error(f"주문 실패: {response.message}")
                all_orders_successful = False

        # 주문 완료 후 처리
        if all_orders_successful:
            messagebox.showinfo("주문 완료", "모든 주문이 완료되었습니다.")
        else:
            messagebox.showerror("주문 실패", "일부 주문이 실패했습니다.")

        # 주문 완료 후 주문 내역 초기화
        self.order = {}
        self.total_price = 0.0
        self.update_order_list()  # 주문 내역 갱신하여 비우기
        self.order_placed = False  # 주문 완료 플래그 초기화

    def add_to_order(self, item):
        """주문 항목 추가"""
        if item not in self.order:
            self.order[item] = 1
        else:
            self.order[item] += 1
        self.update_order_list()

    def update_order_list(self):
        """주문 내역 갱신"""
        self.order_listbox.delete(0, "end")
        for item, quantity in self.order.items():
            self.order_listbox.insert("end", f"{item} x{quantity}")

    def on_closing(self):
        """윈도우 종료 처리"""
        # Tkinter 이벤트 루프 종료 후 ROS 종료
        self.root.quit()  # Tkinter 이벤트 루프 종료
        rclpy.shutdown()  # ROS 2 종료


def run_menu_gui(table_num):
    """각 테이블에 대한 GUI 실행 함수"""
    menu_gui = MenuGUI(table_num)
    menu_gui.root.mainloop()  # Tkinter 이벤트 루프 실행


def main(args=None):
    """메인 함수"""
    rclpy.init(args=args)

    # 멀티스레딩을 사용하여 각 테이블의 GUI 실행
    threads = []
    for table_num in range(1, 3):
        thread = threading.Thread(target=run_menu_gui, args=(table_num,))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 종료될 때까지 대기
    for thread in threads:
        thread.join()


    rclpy.shutdown()


if __name__ == '__main__':
    main()

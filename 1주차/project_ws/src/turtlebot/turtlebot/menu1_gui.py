import rclpy
from rclpy.node import Node
from tkinter import messagebox, Tk, Button, Listbox, Frame, Label
from order_msgs.srv import Order  # 주문 서비스 임포트
from PIL import Image, ImageTk  # 이미지 처리용


class MenuGUI(Node):
    def __init__(self):
        super().__init__('menu_gui')

        # ROS 2 클라이언트 초기화
        self.cli = self.create_client(Order, 'order')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('서비스가 아직 준비되지 않았습니다...')
        
        # GUI 초기화
        self.root = Tk()
        self.root.configure(bg="#F5F3EF")
        self.root.title("1번 테이블")

        # 메뉴 항목 정의
        self.menu_items = {
            "아이스 아메리카노": (2500, "/home/rokey/Desktop/project_ws/ame1.jpg"),
            "아이스 라떼": (2500, "/home/rokey/Desktop/project_ws/ra1.jpg"),
            "감자한알": (1000, "/home/rokey/Desktop/project_ws/pota1.jpg"),
            "뽀로로 케이크": (13000, "/home/rokey/Desktop/project_ws/pororo1.jpg")
        }

        # 주문 내역과 총 가격 초기화
        self.order = {}
        self.total_price = 0.0

        # 메뉴 화면 설정
        row = 1
        Label(self.root, text="Cafe menu", font=("Arial", 16), bg="#F5F3EF", fg="#463728").grid(row=0, column=0, columnspan=2, padx=(0, 10))
        
        # 메뉴 항목 표시 및 버튼 추가
        self.images = {}
        for index, (item, (price, image_path)) in enumerate(self.menu_items.items()):
            try:
                image = Image.open(image_path)
                image = image.resize((100, 100), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.images[item] = photo
                
                # 메뉴 항목 이미지와 버튼 배치
                row_offset = (index // 2) * 2
                Label(self.root, image=photo).grid(row=row + row_offset, column=index % 2, padx=(10, 5), pady=5)
                Button(self.root, text=f"{item} - {price}원", command=lambda item=item: self.add_to_order(item), bg="#F5F3EF", fg="#463728").grid(row=row + row_offset + 1, column=index % 2, padx=5, pady=(0, 10))
            except Exception as e:
                self.get_logger().warn(f"이미지 로딩 실패: {image_path} ({e})")
                
        # 주문 내역 표시
        order_frame = Frame(self.root)
        order_frame.grid(row=1, column=2, rowspan=5, columnspan=2, sticky="ns", padx=15, pady=5)
        self.order_listbox = Listbox(order_frame, width=30)
        self.order_listbox.pack(side="left", fill="both", expand=True)
        
        # 수량 조정 및 삭제 버튼
        Button(self.root, text="+", command=self.increase_order, bg="#F5F3EF", fg="#463728").grid(row=row + 7, column=2, padx=5, pady=5)
        Button(self.root, text="-", command=self.decrease_order, bg="#F5F3EF", fg="#463728").grid(row=row + 7, column=3, padx=5, pady=5)
        Button(self.root, text="삭제", command=self.delete_order, bg="#F5F3EF", fg="#463728").grid(row=row + 7, column=2, columnspan=2, padx=5, pady=5)
        
        # 주문 버튼
        order_button = Button(self.root, text="주문하기", command=self.place_order, width=10, bg="#F5F3EF")
        order_button.grid(row=row + 9, column=2, columnspan=2, padx=5, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def increase_order(self):
        """주문 내역에서 선택된 항목의 수량 증가"""
        selected_index = self.order_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("경고", "수량을 증가시킬 항목을 선택하세요.")
            return

        item = self.order_listbox.get(selected_index).split(" x")[0]
        self.order[item] += 1
        self.update_order_list(selected_index[0])

    def decrease_order(self):
        """주문 내역에서 선택된 항목의 수량 감소"""
        selected_index = self.order_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("경고", "수량을 감소시킬 항목을 선택하세요.")
            return

        item = self.order_listbox.get(selected_index).split(" x")[0]
        if self.order[item] > 1:
            self.order[item] -= 1
        else:
            messagebox.showwarning("경고", "수량은 1 이상이어야 합니다.")
        self.update_order_list(selected_index[0])

    def delete_order(self):
        """주문 내역에서 선택된 항목 삭제"""
        selected_index = self.order_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("경고", "삭제할 항목을 선택하세요.")
            return

        item = self.order_listbox.get(selected_index).split(" x")[0]
        del self.order[item]
        self.update_order_list()

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
            price = self.menu_items[item][0]
            order_request = Order.Request()
            order_request.table_num = "1"  # 예시로 테이블 번호 1로 설정
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

    def update_order_list(self, selected_index=None):
        """주문 내역 갱신"""
        self.order_listbox.delete(0, "end")
        for item, quantity in self.order.items():
            self.order_listbox.insert("end", f"{item} x{quantity}")
            
        if selected_index is not None and selected_index < self.order_listbox.size():
            self.order_listbox.selection_set(selected_index)
        

    def on_closing(self):
        """윈도우 종료 처리"""
        rclpy.shutdown()
        self.root.quit()


def main(args=None):
    rclpy.init(args=args)
    menu_gui = MenuGUI()
    rclpy.spin(menu_gui)
    menu_gui.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

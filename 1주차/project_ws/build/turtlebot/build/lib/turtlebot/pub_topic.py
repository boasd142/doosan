#!/usr/bin/env python3

import rclpy  # 수정: rpy를 rclpy로 변경
from rclpy.node import Node
from std_msgs.msg import String
import tkinter as tk
from tkinter import ttk
import threading

class PublisherGUI(Node):
    def __init__(self):
        super().__init__('publisher_gui')
        self.publisher = self.create_publisher(String, 'order_topic', 10)
        self.root = tk.Tk()
        self.root.title("ROS2 Publisher GUI")

        # 전체 창의 배경색 설정
        self.root.configure(bg='lightgray')
        self.root.geometry("500x600")  # 인터페이스 크기 조정

        self.main_frame = ttk.Frame(self.root, padding="10", relief=tk.SUNKEN)
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Frame의 스타일 설정
        style = ttk.Style()
        style.configure("TFrame", background="lightgray")
        self.main_frame.configure(style="TFrame")

        self.menu_items = ["아이스 아메리카노", "아이스 라떼", "케이크"]
        self.prices = [3500, 4500, 5500]  # 각 메뉴의 가격
        self.selected_orders = {}

        self.status_var = tk.StringVar(value="주문을 선택하세요")
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var, background='lightgray', font=("Helvetica", 12))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=5)

        self.order_summary_var = tk.StringVar(value="")
        self.order_summary_label = ttk.Label(self.main_frame, textvariable=self.order_summary_var, background='white', width=40, anchor="w", justify="left")
        self.order_summary_label.grid(row=1, column=0, columnspan=3, pady=5, sticky="ew")

        self.create_menu_buttons()  # 메뉴 버튼 생성
        self.create_order_space()  # 주문 추가 공간 생성

        self.order_button = ttk.Button(self.main_frame, text="주문하기", command=self.confirm_order)
        self.order_button.grid(row=5, column=2, pady=5, sticky="e")  # 우측 맨 아래로 배치

        # 라벨과 버튼의 크기 조정
        for column in range(3):
            self.main_frame.columnconfigure(column, weight=1)

    def create_menu_buttons(self):
        # 메뉴 버튼과 가격을 생성하는 부분
        for i, item in enumerate(self.menu_items):
            button = ttk.Button(self.main_frame, text=item, command=lambda item=item: self.add_order(item))
            button.grid(row=3, column=i, padx=5, pady=5, sticky="ew")  # 메뉴 버튼을 주문 내역 관리용 프레임 아래로 이동

            # 가격 레이블 추가
            price_label = ttk.Label(self.main_frame, text=f"{self.prices[i]}원", background='lightgray', font=("Helvetica", 10))
            price_label.grid(row=4, column=i, pady=5)

    def create_order_space(self):
        # 추가 주문을 위한 공간을 생성
        self.additional_order_frame = ttk.Frame(self.main_frame, padding="10")
        self.additional_order_frame.grid(row=2, column=0, columnspan=3, pady=5, sticky="ew")

    def add_order(self, order_item):
        # 해당 메뉴 항목의 수량을 추가
        if order_item in self.selected_orders:
            self.selected_orders[order_item] += 1
        else:
            self.selected_orders[order_item] = 1
        
        self.status_var.set(f'추가됨: "{order_item}"')
        self.get_logger().info(f'추가됨: "{order_item}"')

        self.update_order_summary()
        self.create_order_controls(order_item)  # 주문 조절 버튼 생성

    def create_order_controls(self, order_item):
        # 주문 수량 조절을 위한 버튼 생성
        order_frame = ttk.Frame(self.additional_order_frame)
        order_frame.pack(side=tk.TOP, fill=tk.X)

        # 수량 감소 버튼 (왼쪽 정렬)
        remove_button = ttk.Button(order_frame, text="-", command=lambda item=order_item: self.change_order(item, -1))
        remove_button.pack(side=tk.LEFT)

        count_label = ttk.Label(order_frame, text=f"{order_item} x {self.selected_orders[order_item]}개", background='lightgray', anchor="center")
        count_label.pack(side=tk.LEFT, padx=5, expand=True)  # 가운데 정렬

        # 수량 증가 버튼 (왼쪽 정렬)
        add_button = ttk.Button(order_frame, text="+", command=lambda item=order_item: self.change_order(item, 1))
        add_button.pack(side=tk.LEFT)

    def change_order(self, order_item, change):
        if order_item in self.selected_orders:
            self.selected_orders[order_item] += change
            if self.selected_orders[order_item] <= 0:
                del self.selected_orders[order_item]  # 수량이 0 이하일 경우 삭제
            self.update_order_summary()  # 주문 요약 업데이트

            # 주문 항목 표시 업데이트
            self.update_order_controls()

    def update_order_controls(self):
        # 주문 수량 표시 업데이트
        for widget in self.additional_order_frame.winfo_children():
            widget.destroy()  # 이전 위젯 제거

        for item in self.selected_orders:
            self.create_order_controls(item)  # 수량 조절 버튼 재생성

    def update_order_summary(self):
        summary = ""
        for item in self.menu_items:
            count = self.selected_orders.get(item, 0)
            if count > 0:
                summary += f"{item} x {count}개\n"  # 형식 변경

        self.order_summary_var.set(summary.strip())

    def confirm_order(self):
        if not self.selected_orders:
            self.status_var.set("주문이 없습니다.")
            return

        total_price = 0
        order_summary = ""
        for i, item in enumerate(self.menu_items):
            count = self.selected_orders.get(item, 0)
            if count > 0:
                order_summary += f"{item} x {count}개\n"
                total_price += count * self.prices[i]

        order_summary += f"\n총 금액: {total_price}원"

        self.show_confirmation_popup(order_summary)

    def show_confirmation_popup(self, order_summary):
        popup = tk.Toplevel(self.root)
        popup.title("주문 확인")
        
        confirmation_label = ttk.Label(popup, text="주문 내역:")
        confirmation_label.pack(pady=5)

        order_text = tk.Text(popup, height=10, width=40)
        order_text.insert(tk.END, order_summary)
        order_text.pack(pady=5)

        confirm_button = ttk.Button(popup, text="주문 완료", command=lambda: self.complete_order(popup))
        confirm_button.pack(pady=5)

        cancel_button = ttk.Button(popup, text="취소", command=popup.destroy)
        cancel_button.pack(pady=5)

    def complete_order(self, popup):
        orders_msg = String()
        orders_str = ', '.join([f'{item} x {count}' for item, count in self.selected_orders.items()])
        total_price = sum(self.selected_orders[item] * self.prices[self.menu_items.index(item)] for item in self.selected_orders)
        orders_msg.data = f"주문: {orders_str}, 총 금액: {total_price}원"
        self.publisher.publish(orders_msg)

        self.selected_orders.clear()
        self.status_var.set("주문 완료")
        self.order_summary_var.set("")  # 주문 완료 후 주문 내용 삭제
        self.get_logger().info(f'주문 완료: "{orders_msg.data}"')

        popup.destroy()  # 팝업 닫기

    def run(self):
        self.ros_thread = threading.Thread(target=self._spin_ros, daemon=True)
        self.ros_thread.start()
        self.root.mainloop()

    def _spin_ros(self):
        rclpy.spin(self)

def main(args=None):
    rclpy.init(args=args)  # 수정: rpy를 rclpy로 변경
    node = PublisherGUI()

    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

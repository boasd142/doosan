import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class DeliveryRobotInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("배달 로봇 인터페이스")
        self.setGeometry(100, 100, 600, 450)  # 창 크기 증가
        
        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)  # 세로 중앙 정렬
        main_layout.setContentsMargins(10, 10, 10, 10)  # 여백 최소화
        self.setLayout(main_layout)

        # 테이블 번호 라벨
        self.table_number_label = QLabel("테이블 번호: 대기 중")
        self.table_number_label.setAlignment(Qt.AlignCenter)  # 중앙 정렬
        self.table_number_label.setFont(QFont("Arial", 20))  # 글자 크기 증가
        main_layout.addWidget(self.table_number_label)
        
        # 주문 내역 레이아웃
        self.orders_layout = QVBoxLayout()
        self.orders_layout.setAlignment(Qt.AlignCenter)  # 세로 중앙 정렬
        main_layout.addLayout(self.orders_layout)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        self.complete_button = QPushButton("배달 완료")
        self.call_staff_button = QPushButton("직원 호출")

        # 버튼 크기 조정
        self.complete_button.setFont(QFont("Arial", 16))  # 버튼 글자 크기 증가
        self.call_staff_button.setFont(QFont("Arial", 16))
        self.complete_button.setFixedHeight(60)  # 버튼 높이 증가
        self.call_staff_button.setFixedHeight(60)

        button_layout.addWidget(self.complete_button)
        button_layout.addWidget(self.call_staff_button)
        main_layout.addLayout(button_layout)

    def update_order(self, table_number, orders):
        # 테이블 번호 업데이트
        self.table_number_label.setText(f"테이블 번호: {table_number}")

        # 기존 주문 내역 제거
        for i in reversed(range(self.orders_layout.count())): 
            self.orders_layout.itemAt(i).widget().setParent(None)

        # 주문 내역 추가
        for menu_name, quantity, price in orders:
            item_layout = QHBoxLayout()
            menu_label = QLabel(menu_name)
            qty_label = QLabel(f"{quantity}개")
            price_label = QLabel(f"{price}원")
            
            # 텍스트 중앙 정렬 및 글자 크기 증가
            menu_label.setAlignment(Qt.AlignCenter)
            qty_label.setAlignment(Qt.AlignCenter)
            price_label.setAlignment(Qt.AlignCenter)
            menu_label.setFont(QFont("Arial", 16))
            qty_label.setFont(QFont("Arial", 16))
            price_label.setFont(QFont("Arial", 16))

            item_layout.addWidget(menu_label)
            item_layout.addWidget(qty_label)
            item_layout.addWidget(price_label)
            
            self.orders_layout.addLayout(item_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeliveryRobotInterface()

    # 예시 주문 추가 (테이블 번호와 주문 목록)
    example_orders = [
        ("아이스 아메리카노", 2, 2500),
        ("카페 라떼", 1, 2500),
        ("뽀로로 케이크", 1, 13000)
    ]
    window.update_order(5, example_orders)  # 테이블 번호 5번에 주문 추가

    window.show()
    sys.exit(app.exec_())


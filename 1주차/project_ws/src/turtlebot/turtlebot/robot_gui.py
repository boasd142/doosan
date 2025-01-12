import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus

from rclpy.qos import QoSDurabilityPolicy
from rclpy.qos import QoSHistoryPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy


class DeliveryRobotInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 450)
        self.setStyleSheet("""
            background-color: #F5F3EF;
            color: #463728;
        """)

        # 메인 레이아웃 설정
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 40, 0, 0)
        self.setLayout(self.main_layout)

        # 테이블 번호 라벨
        self.table_number_label = QLabel("대기중")
        self.table_number_label.setAlignment(Qt.AlignCenter)
        self.table_number_label.setFont(QFont("Arial", 38))
        self.main_layout.addWidget(self.table_number_label)

        # 주문 내역 공간 추가
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout.addSpacerItem(spacer)

        # 주문 내역 레이아웃
        self.orders_layout = QVBoxLayout()
        self.orders_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.addLayout(self.orders_layout)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        self.complete_button = QPushButton("배달 완료")
        self.call_staff_button = QPushButton("직원 호출")
        self.complete_button.setFont(QFont("Arial", 16))
        self.call_staff_button.setFont(QFont("Arial", 16))
        self.complete_button.setFixedHeight(60)
        self.call_staff_button.setFixedHeight(60)
        button_layout.addWidget(self.complete_button)
        button_layout.addWidget(self.call_staff_button)
        self.main_layout.addStretch()
        self.main_layout.addLayout(button_layout)

        # 팝업 창 설정
        self.popup = QWidget(self)
        self.popup.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.popup.setStyleSheet("background-color: #F5F3EF; color: #463728; border: 2px solid #463728;")
        
        popup_layout = QVBoxLayout()  # 잘못된 들여쓰기 수정
        popup_label = QLabel("^                  ^\n_________\n\n맛있게 드세요")
        popup_label.setAlignment(Qt.AlignCenter)
        popup_label.setFont(QFont("Arial", 30))
        popup_label.setStyleSheet("color: #463728;")
        popup_layout.addWidget(popup_label)
        self.popup.setLayout(popup_layout)
        self.popup.setVisible(False)

        # 주방 좌표 설정
        self.kitchen_room = [0.73, 4.0]

        # ROS2 노드
        self.node = DeliveryRobotNode(self)

        # 버튼 클릭 이벤트 연결
        self.complete_button.clicked.connect(self.show_popup)

    def show_popup(self):
        # 팝업 창 표시
        self.popup.setGeometry(self.geometry().x() + 10, self.geometry().y() + 10, self.width() - 20, self.height() - 100)
        self.popup.setVisible(True)
        QTimer.singleShot(5000, self.hide_popup)
        self.node.navigate_to_pose_send_goal(self.kitchen_room)

    def hide_popup(self):
        self.popup.setVisible(False)
        self.update_order("대기중", [])

    def update_order(self, table_number, orders):
        self.table_number_label.setText(f"{table_number} 테이블 - 배달 중" if table_number != "대기중" else "대기중")
        for i in reversed(range(self.orders_layout.count())):
            self.orders_layout.itemAt(i).widget().setParent(None)
        for order in orders:
            item_label = QLabel(order)
            item_label.setAlignment(Qt.AlignCenter)
            item_label.setFont(QFont("Arial", 20))
            self.orders_layout.addWidget(item_label)


class DeliveryRobotNode(Node):
    def __init__(self, gui):
        super().__init__('delivery_robot_node')
        self.gui = gui

        # qos프로파일 설정
        QoS_CALL = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL)
        '''
            주방에서 호출메세지를 받는 subscriber에 사용
            reliable을 이용해 손실되지 않도록 함
            keep_last와 depth=1로 설정해 최신 호출을 받아들인다
            transient_local 설정으로 시스템 재시작시에도 마지막 호출은 남아있음
        '''

        # 직원 호출 퍼블리셔
        self.call_staff_publisher = self.create_publisher(String, 'call_staff', QoS_CALL)
        self.current_table_number = ""

        # 직원 호출 버튼 연결
        gui.call_staff_button.clicked.connect(self.call_staff)

        # 주문 정보 수신 서브스크라이버
        self.delivery_info_subscriber = self.create_subscription(
            String, 'table_delivery_info', self.delivery_info_callback, 10
        )

        # NavigateToPose 액션 클라이언트
        self.navigate_to_pose_action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def delivery_info_callback(self, msg):
        table_info, order_data = msg.data.split(": ", 1)
        table_number = table_info.split(" ")[0]
        order_details = order_data.split(", ")
        self.gui.update_order(table_number, order_details)
        self.current_table_number = table_number

    def call_staff(self):
        msg = String()
        msg.data = f"{self.current_table_number} 테이블 호출"
        self.call_staff_publisher.publish(msg)
        self.get_logger().info(f"{msg.data} 메시지를 발행했습니다.")

    def navigate_to_pose_send_goal(self, goal):
        if not self.navigate_to_pose_action_client.wait_for_server(timeout_sec=3.0):
            self.get_logger().warning('Navigate action server is not available.')
            return

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = "map"
        goal_msg.pose.pose.position.x = goal[0]
        goal_msg.pose.pose.position.y = goal[1]
        goal_msg.pose.pose.orientation.x = 0.0
        goal_msg.pose.pose.orientation.y = 0.0
        goal_msg.pose.pose.orientation.z = -0.787
        goal_msg.pose.pose.orientation.w = 0.707

        self.get_logger().info('Sending navigation goal...')
        send_goal_future = self.navigate_to_pose_action_client.send_goal_async(
            goal_msg, feedback_callback=self.navigate_to_pose_action_feedback
        )
        send_goal_future.add_done_callback(self.navigate_to_pose_action_goal)

    def navigate_to_pose_action_goal(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().warning('Action goal rejected.')
            return
        self.get_logger().info('Action goal accepted.')
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.navigate_to_pose_action_result)

    def navigate_to_pose_action_feedback(self, feedback_msg):
        self.get_logger().info('Feedback received.')

    def navigate_to_pose_action_result(self, future):
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Navigation succeeded.')
        else:
            self.get_logger().warning('Navigation failed.')


def main():
    rclpy.init()
    app = QApplication(sys.argv)
    gui = DeliveryRobotInterface()
    gui.show()

    timer = gui.startTimer(100)
    
    def spin_once():
        rclpy.spin_once(gui.node, timeout_sec=0.1)
        
    gui.timerEvent = lambda event: spin_once()

    app.exec_()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

import rclpy
import sys

import mysql.connector
from mysql.connector import Error

from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import QTimer  # For periodic updates

from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import GoalStatus
from rclpy.callback_groups import ReentrantCallbackGroup

from std_msgs.msg import String
from order_msgs.srv import Order  # 서비스 임포트
from geometry_msgs.msg import Point, Quaternion

from nav2_msgs.srv import SetInitialPose
from nav2_msgs.action import NavigateToPose

from rclpy.qos import QoSDurabilityPolicy
from rclpy.qos import QoSHistoryPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy

class KitchenInterface(Node, QWidget):  # Inherit both Node and QWidget
    def __init__(self):
        super().__init__('kitchen_interface')  # Initialize ROS 2 Node
        QWidget.__init__(self)  # Initialize QWidget (PyQt)

        self.setWindowTitle("주문 내역")
        self.setGeometry(100, 100, 800, 600)
        
        # 주문번호
        self.order_id = 1
        
        # 로봇 초기 좌표 pose:x,y orient:z,w
        self.init_pose = [0.73, 4.0, 0.0, 1.0]
        
        # 각 테이블 좌표
        self.goal_poses = [[1.78, 3.1], [1.79,1.98], [1.72,0.866],
                           [0.7, 3.14], [0.68, 1.96], [0.6, 0.9], 
                           [-0.42, 3.14], [-0.43, 2.03], [-0.477, 0.971]]

        # ROS 2 서비스 서버 설정
        self.callback_group = ReentrantCallbackGroup()
        
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
        
        self.kitchen_service_server = self.create_service(
            Order,
            'order',
            self.get_order,
            callback_group=self.callback_group
        )

        # 배달 로봇에 퍼블리싱 할 퍼블리셔
        self.delivery_publisher = self.create_publisher(
            String,
            'table_delivery_info',
            10
        )
        
        # 호출 섭스크립션
        self.call_staff_subscriber = self.create_subscription(
            String,
            'call_staff',
            self.staff_callback,
            QoS_CALL
        )

        # 로봇 초기위치 서비스 클라이언트
        self.set_initial_pose_service_client = self.create_client(
            SetInitialPose,
            '/set_initial_pose'
        )
        
        # 액션 클라이언트
        self.navigate_to_pose_action_client = ActionClient(
          self,
          NavigateToPose,
          'navigate_to_pose'
        )
       
       
        while not self.set_initial_pose_service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service /set_initial_pose not available, waiting again...')
        self.set_initial_pose(*self.init_pose)


        #DB연결
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='turtlebot',
                user='root',
                password='rnjsrms9'
            )
            if self.connection.is_connected():
                self.get_logger().info('Successfully connected to MySQL DB')
        except Error as e:
            self.get_logger().error(f"Error while connecting to MySQL: {e}")
            


        # 테이블 생성
        self.table_orders = []  # 테이블 주문 내역 저장

        layout = QGridLayout()  # Use QGridLayout for grid-like arrangement
        for i in range(9):
            table_box = QGroupBox(f"테이블 {i+1}")
            table_layout = QVBoxLayout()
            
            # 기본 상태로 "대기 중" 라벨 추가
            waiting_label = QLabel("대기 중")
            table_layout.addWidget(waiting_label)

            # 주문 내역 및 총 가격 레이블 초기화
            orders_layout = QVBoxLayout()
            total_price_label = QLabel("총 가격: 0원")
            total_price_label.setVisible(False)  # 주문이 들어올 때만 표시

            # 드래그 가능한 주문 목록 (QListWidget)
            order_list_widget = QListWidget()
            order_list_widget.setDragEnabled(True)  # 드래그 활성화
            orders_layout.addWidget(order_list_widget)
            
            # 버튼 레이아웃
            button_layout = QHBoxLayout()
            depart_button = QPushButton("출발")
            depart_button.setVisible(False)
            depart_button.clicked.connect(lambda _, i=i: self.on_depart_button_click(i))  # 테이블 번호 전달, 로봇 action_goal 전달
            button_layout.addWidget(depart_button)

            # 레이아웃에 추가
            table_layout.addLayout(orders_layout)
            table_layout.addWidget(total_price_label)
            table_layout.addLayout(button_layout)

            # 그룹박스 설정
            table_box.setLayout(table_layout)
            layout.addWidget(table_box, i // 3, i % 3)  # Use QGridLayout for placing widgets in a 3x3 grid

            # 각 테이블 상태 관리
            self.table_orders.append({
                "table_box": table_box,
                "waiting_label": waiting_label,
                "orders_layout": orders_layout,
                "total_price_label": total_price_label,
                "depart_button": depart_button,
                "total_price": 0,
                "order_list_widget": order_list_widget

            })

        self.setLayout(layout)  # Set the main window layout

        # Create a QTimer to periodically call rclpy.spin_once()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.spin_once)
        self.timer.start(100)  # Spin every 100 ms

    def staff_callback(self, msg):
        self.get_logger().info(f"직원 호출 요청 수신: {msg.data}")
        

    def spin_once(self):
        rclpy.spin_once(self, timeout_sec=0.1)

    def get_order(self, request, response):
        table_num = int(request.table_num) - 1  # 테이블 번호 (0-based index)
        item = request.item
        quantity = request.quantity
        price = request.price

        menu_to_db_mapping = {
            "아이스 아메리카노": "coffee",
            "뽀로로 케이크": "cake",
            "아이스 라떼": "latte",
            "감자한알": "potato",
        }

        # 주문 처리 시
        item_name_in_db = menu_to_db_mapping.get(item, item)

        try:
            cursor = self.connection.cursor()

            # MySQL 재고 수량 확인
            check_quantity_query = "SELECT item_stock FROM item WHERE item_name = %s"
            cursor.execute(check_quantity_query, (item_name_in_db,))
            result = cursor.fetchone()
            
            # 재고 확인
            available_quantity = result[0]
            
            # 재고 부족 시 주문 거절
            if available_quantity < quantity:
                self.get_logger().warn(f"{request.table_num}번 테이블에서 {item} {quantity}개 주문을 받았으나 재고가 없습니다.")
                response.success = False
                response.message = f"{item}의 재고가 부족하여 주문을 접수할 수 없습니다."
                return response
            
            # 주문 접수
            else:
                self.get_logger().info(f"{request.table_num}번 테이블에서 {item} {quantity}개 주문이 접수 되었습니다.")

##
                update_order_query = "INSERT INTO orders (order_id, table_num, item_name, item_num, item_price) VALUES (%s,%s+1,%s,%s,%s*%s)"
                cursor.execute(update_order_query, (self.order_id, table_num, item_name_in_db, quantity, quantity, price))
                    
                self.connection.commit()
                self.order_id += 1
##

                # 주문 내역 출력
                self.add_order(table_num, item, quantity, price)

                # 재고 수량 업데이트
                update_quantity_query = "UPDATE item SET item_stock = item_stock - %s WHERE item_name = %s"
                cursor.execute(update_quantity_query, (quantity, item_name_in_db))
                self.connection.commit()
                
                # 응답 처리
                response.success = True
                response.message = f"{request.table_num}번 테이블 {item} {quantity}개 주문이 접수되었습니다."
                return response            

        except Error as e:
            # 예외 발생 시 응답 실패 처리
            response.success = False
            response.message = f"재고 업데이트 중 오류 발생: {str(e)}"
            self.connection.rollback()  # 오류 발생 시 롤백하여 데이터베이스 상태를 유지
    
        finally:
            cursor.close()
            self.get_logger().info("DB cursor 종료")



    def add_order(self, table_index, menu_name, quantity, price):
        """주문을 해당 테이블에 추가"""
        table_order = self.table_orders[table_index]
        
        # "대기 중" 라벨 숨기기
        table_order["waiting_label"].setVisible(False)
        
        # 주문 항목 리스트에서 이미 같은 메뉴가 있는지 확인
        existing_item = None
        for index in range(table_order["order_list_widget"].count()):
            item = table_order["order_list_widget"].item(index)
            if menu_name in item.text():  # 메뉴 이름이 포함되어 있으면 같은 주문으로 간주
                existing_item = item
                break

        if existing_item:
            # 이미 있는 주문 항목이 있으면 수량을 업데이트
            current_quantity = int(existing_item.text().split("x")[1].split("-")[0].strip())
            new_quantity = current_quantity + quantity
            existing_item.setText(f"{menu_name} x{new_quantity} - {price * new_quantity}원")
        else:
            # 새로운 메뉴 항목 추가
            order_text = f"{menu_name} x{quantity} - {price * quantity}원"
            item = QListWidgetItem(order_text)
            table_order["order_list_widget"].addItem(item)

        # 총 가격 업데이트 및 표시
        table_order["total_price"] += price * quantity
        table_order["total_price_label"].setText(f"총 가격: {table_order['total_price']}원")
        table_order["total_price_label"].setVisible(True)

        # 버튼 활성화
        table_order["depart_button"].setVisible(True)

        # 버튼 상태 변경 (접수 완료 / 출발 준비 완료)
        table_order["depart_button"].setText("배달 준비 완료")
        table_order["depart_button"].setEnabled(True)

    def on_depart_button_click(self, table_index):
        """출발 버튼 클릭 시 호출되는 함수"""
        table_order = self.table_orders[table_index]
        order_details = []

        for index in range(table_order["order_list_widget"].count()):
            item_text = table_order["order_list_widget"].item(index).text()
            order_details.append(item_text)

        # 테이블 번호와 주문 내용을 포함한 메시지 생성 및 발행
        msg = String()
        msg.data = f"{table_index + 1}번 테이블: {', '.join(order_details)}"
        self.delivery_publisher.publish(msg)
        self.get_logger().info(f"{table_index + 1}번 테이블의 주문 정보가 Robot GUI로 전송되었습니다.")

        self.navigate_to_pose_send_goal(table_index)
   
    
    def set_initial_pose(self, x,y,z,w):
        req = SetInitialPose.Request()
        req.pose.header.frame_id = 'map'
        req.pose.pose.pose.position = Point(x=x, y=y, z=0.0)
        req.pose.pose.pose.orientation = Quaternion(x=0.0, y=0.0, z=z, w=w)
        req.pose.pose.covariance = [0.1, 0.0, 0.0, 0.0, 0.0, 0.1,

                              0.0, 0.0, 0.0, 0.0, 0.0, 0.0,

                              0.0, 0.0, 0.1, 0.0, 0.0, 0.0,

                              0.0, 0.0, 0.0, 0.01, 0.0, 0.0,

                              0.0, 0.0, 0.0, 0.0, 0.01, 0.0,

                              0.0, 0.0, 0.0, 0.0, 0.0, 0.01]
                              
        future = self.set_initial_pose_service_client.call_async(req)
        
        if future.result() is not None:
           self.get_logger().info("Initial pose set successfully")
        else:
           self.get_logger().warning("Failed to set initial pose")
           
        return future.result()
    
    def navigate_to_pose_send_goal(self, table_index):
        wait_count = 1
        while not self.navigate_to_pose_action_client.wait_for_server(timeout_sec=0.1):
            if wait_count >3:
                self.get_logger().warning('Navigate action server is not availavle.')
                return False
            wait_count += 1
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = "map"
        goal_msg.pose.pose.position.x = self.goal_poses[table_index][0]
        goal_msg.pose.pose.position.y = self.goal_poses[table_index][1]
        goal_msg.pose.pose.position.z = 0.0
        goal_msg.pose.pose.orientation.x = 0.0
        goal_msg.pose.pose.orientation.y = 0.0
        goal_msg.pose.pose.orientation.z = -0.787
        goal_msg.pose.pose.orientation.w = 0.707
        
        self.send_goal_future = self.navigate_to_pose_action_client.send_goal_async(
            goal_msg,
            feedback_callback = self.navigate_to_pose_action_feedback
        )
        self.send_goal_future.add_done_callback(self.navigate_to_pose_action_goal)
        
    def navigate_to_pose_action_goal(self, future):
        goal_handle = future.result()
        
        if not goal_handle.accepted:
            self.get_logger().warning('Action goal refected.')
            return
            
        self.get_logger().info('Action goal accepted.')
        
        self.action_result_future = goal_handle.get_result_async()
        self.action_result_future.add_done_callback(self.navigate_to_pose_action_result)
        
    def navigate_to_pose_action_feedback(self, feedback_msg):
        action_feedback = feedback_msg.feedback
        #self.get_logger().info("Action feedback: {0}".format(action_feedback))
        
    def navigate_to_pose_action_result(self, future):
        action_status = future.result().status
        action_result = future.result().result
        
        if action_status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Action succeeded.')
        else:
            self.get_logger().warning('Action failed.') 



def main(args=None):
    rclpy.init(args=args)
    app = QApplication(sys.argv)

    kitchen_interface = KitchenInterface()
    kitchen_interface.show()
    
    app.exec_()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

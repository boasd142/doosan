import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tkinter import Tk, Canvas, Label
from PIL import Image as PILImage, ImageTk
import yaml
from pathlib import Path
import threading

from cv_bridge import CvBridge

from sensor_msgs.msg import Image as ROSImage
from std_msgs.msg import Int32

from nav2_msgs.action import FollowWaypoints
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped,Point

import math

class OdomNode(Node):
    def __init__(self, map_viewer):
        super().__init__('odom_listener')
        self.map_viewer = map_viewer

        # '/tb1/odom' 토픽 구독
        self.subscription_tb1 = self.create_subscription(
            Odometry,
            '/tb1/odom',
            self.odom_callback_tb1,
            10
        )

        # '/tb2/odom' 토픽 구독
        self.subscription_tb2 = self.create_subscription(
            Odometry,
            '/tb2/odom',
            self.odom_callback_tb2,
            10
        )

        # '/tb1/camera/image_raw' 토픽 구독
        self.subscription_tb1_camera = self.create_subscription(
            ROSImage,
            '/tb1/camera/image_raw',
            self.tb1_camera_callback,
            10
        )

        # '/tb2/camera/image_raw' 토픽 구독
        self.subscription_tb2_camera = self.create_subscription(
            ROSImage,
            '/tb2/camera/image_raw',
            self.tb2_camera_callback,
            10
        )

        # 도둑 스폰 토픽 구독
        self.thief_subscription = self.create_subscription(
            Int32,
            '/thief_spawn',
            self.thief_spawn_callback,
            10
        ) 

        # 도둑 스폰 시 tb1 이동 퍼블리셔
        self.tb1_find_publisher = ActionClient(
            self,
            FollowWaypoints,
            '/tb1/follow_waypoints'
        )

        self.find_thief_subscription = self.create_subscription(
            Point,
            '/thief_point',
            self.point_callback,
            10
        )

        # 위치 확인 후, 2번 경찰로봇 호출
        self.call_tb2 = self.create_publisher(
            Point,
            'thief_point_up',
            10
        )
        
        # cancel_goal 관련 변수
        self._goal_handle = None
        self.is_goal_completed = False

        # 초기 위치 설정
        self.x_tb2 = 0.0
        self.y_tb2 = 0.0
        self.x_tb1 = 0.0
        self.y_tb1 = 0.0

        # 회전 (orientation) 정보 저장
        self.x_tb2_quat = 0.0
        self.y_tb2_quat = 0.0
        self.z_tb2_quat = 0.0
        self.w_tb2_quat = 1.0  # 초기값 (회전하지 않은 상태)

        self.x_tb1_quat = 0.0
        self.y_tb1_quat = 0.0
        self.z_tb1_quat = 0.0
        self.w_tb1_quat = 1.0  # 초기값 (회전하지 않은 상태)

        # 도둑 스폰 확인
        self.thief_check = False
        self.thief_point = Point()
        self.thief_found = False

        # tb1 도둑 순찰 목표 지점
        self.waypoints = [
            (3.35, 6.53, 0.5),
            (3.26, 4.75, 0.5),
            (3.35, 6.86, 0.5),
            (-4.75, 0.605, 0.5),
            (-0.318, -5.31, 0.5),
            (-4.75, -2.95, 0.5),
            (-2.7, -3.07, 0.5),
            (-0.516, 0.665, 0.5),
        ]
        self.current_waypoint_idx = 0

        # 이미지 변환을 위한 CvBridge 객체
        self.bridge = CvBridge()

    def publish_more_tb(self):
        msg = Point()
        msg.x = self.thief_point.x
        msg.y = self.thief_point.y
        
        self.call_tb2.publish(msg)
        self.get_logger().info(f'증원 요청! 도둑 좌표  x: {msg.x}, y: {msg.y} ')

    def odom_callback_tb2(self, msg):
        """'/tb2/odom' 토픽의 메시지를 처리하는 콜백"""
        self.x_tb2 = msg.pose.pose.position.x
        self.y_tb2 = msg.pose.pose.position.y

        # orientation (회전) 정보를 쿼터니언으로 저장
        self.x_tb2_quat = msg.pose.pose.orientation.x
        self.y_tb2_quat = msg.pose.pose.orientation.y
        self.z_tb2_quat = msg.pose.pose.orientation.z
        self.w_tb2_quat = msg.pose.pose.orientation.w

        self.get_logger().info(f'TB2 Position: x={self.x_tb2}, y={self.y_tb2}')
        self.map_viewer.update_robot_position(self.x_tb2, self.y_tb2, (self.x_tb2_quat, self.y_tb2_quat, self.z_tb2_quat, self.w_tb2_quat), robot='tb2')

    def odom_callback_tb1(self, msg):
        """'/tb1/odom' 토픽의 메시지를 처리하는 콜백"""
        self.x_tb1 = msg.pose.pose.position.x
        self.y_tb1 = msg.pose.pose.position.y

        # orientation (회전) 정보를 쿼터니언으로 저장
        self.x_tb1_quat = msg.pose.pose.orientation.x
        self.y_tb1_quat = msg.pose.pose.orientation.y
        self.z_tb1_quat = msg.pose.pose.orientation.z
        self.w_tb1_quat = msg.pose.pose.orientation.w
        if abs(self.x_tb1 - self.thief_point.x) < 1.0 and abs(self.y_tb1 - self.thief_point.y) < 1.0:
            if self.thief_found == False:
                self.thief_found = True
                self.publish_more_tb()
                if self._goal_handle is not None:
                    self.cancel_goal()
            else:
                pass

        self.get_logger().info(f'TB1 Position: x={self.x_tb1}, y={self.y_tb1}')
        self.map_viewer.update_robot_position(self.x_tb1, self.y_tb1, (self.x_tb1_quat, self.y_tb1_quat, self.z_tb1_quat, self.w_tb1_quat), robot='tb1')

    def tb1_camera_callback(self, msg):
        """'/tb1/camera/image_raw' 토픽의 카메라 이미지를 처리하는 콜백"""
        try:
            # ROS 이미지를 OpenCV 이미지로 변환
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

            # OpenCV 이미지를 Tkinter에서 사용할 수 있는 형식으로 변환
            pil_image = PILImage.fromarray(cv_image)
            self.map_viewer.update_tb1_camera_image(pil_image)
        except Exception as e:
            self.get_logger().error(f"Error converting image: {e}")

    def tb2_camera_callback(self, msg):
        """'/tb2/camera/image_raw' 토픽의 이미지를 처리하는 콜백"""
        try:
            # ROS 이미지를 OpenCV 이미지로 변환
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

            # OpenCV 이미지를 PIL 이미지로 변환하여 Tkinter에서 사용할 수 있도록 함
            pil_image = PILImage.fromarray(cv_image)
            self.map_viewer.update_tb2_camera_image(pil_image)
        except Exception as e:
            self.get_logger().error(f"Error converting image: {e}")

    def send_next_waypoint(self):
        print(self.current_waypoint_idx, "번째 목표 이동 중")
        if self.current_waypoint_idx < len(self.waypoints):
            goal = FollowWaypoints.Goal()

            goal.poses = []
            # 목표 설정
            for waypoint in self.waypoints[self.current_waypoint_idx:]:
                pose = PoseStamped()
                pose.header.frame_id = 'map'
                pose.pose.position.x = waypoint[0]
                pose.pose.position.y = waypoint[1]
                pose.pose.orientation.w = 1.0

                goal.poses.append(pose)
            
            # 목표 발행
            future = self.tb1_find_publisher.send_goal_async(goal, feedback_callback=self.feedback_callback)
            future.add_done_callback(self.goal_handle_callback)
    def goal_handle_callback(self, future):
        """Future에서 실제 GoalHandle 객체를 추출하여 _goal_handle에 저장"""
        try:
            self._goal_handle = future.result()  # 실제 ClientGoalHandle 객체
        except Exception as e:
            self.get_logger().error(f"Goal handling failed: {e}")    

    def feedback_callback(self, feedback_msg):
        current_waypoint = feedback_msg.feedback.current_waypoint
        self.get_logger().info(f'{current_waypoint}번째 waypoint 이동 중')
        if current_waypoint >= len(self.waypoints) - 1:  # 마지막 웨이포인트 도달
            self.is_goal_completed = True

    def thief_spawn_callback(self, msg):
        temp = msg.data
        if temp == 1 and self.thief_found == False:
            self.thief_check = True
            self.get_logger().info("thief_spawn")
            self.send_next_waypoint()
        else:
            pass
    
    def point_callback(self, msg):
        self.thief_point = msg
        self.get_logger().info(f"도둑 위치: x={msg.x}, y={msg.y}")

    def cancel_goal(self):
        if self._goal_handle is not None and not self.is_goal_completed:
            self.get_logger().info("목표를 취소합니다.")
            self.tb1_find_publisher._cancel_goal_async(self._goal_handle)
            self._goal_handle = None
            self.is_goal_completed = False


class MapViewer:
    def __init__(self, root, map_file, resolution, origin):
        self.root = root
        self.map_file = map_file
        self.resolution = resolution
        self.origin = origin

        # 맵 데이터 로드 (YAML 파일에서)
        self.map_data = self.load_map_data(map_file)

        # 맵 이미지 로드
        self.map_image = PILImage.open(self.map_data['image'])

        # 이미지 크기 추출 (픽셀 단위)
        self.map_width, self.map_height = self.map_image.size

        # Tkinter 캔버스 설정
        self.canvas = Canvas(root, width=800, height=800)
        self.canvas.grid(row=0, column=0)

        # 맵 이미지를 800x800 크기로 리사이즈
        self.map_image = self.map_image.resize((800, 800))
        self.map_photo = ImageTk.PhotoImage(self.map_image)

        # 캔버스에 맵 이미지 표시
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_photo)

        # # 로봇 위치를 표시할 점들 (TB2, TB1)
        # self.robot_dot_tb2 = self.canvas.create_oval(
        #     400, 400, 405, 405, fill="red"  # TB2의 초기 위치 (중앙)
        # )
        # self.robot_dot_tb1 = self.canvas.create_oval(
        #     400, 400, 405, 405, fill="blue"  # TB1의 초기 위치 (중앙)
        # )
        # 로봇 위치를 표시할 삼각형들 (TB2, TB1)
        self.robot_triangle_tb2 = self.canvas.create_polygon(
            400, 400, 405, 405, 395, 405,  # TB2의 초기 위치 (중앙)
            fill="red", outline="black"
        )
        self.robot_triangle_tb1 = self.canvas.create_polygon(
            400, 400, 405, 405, 395, 405,  # TB1의 초기 위치 (중앙)
            fill="blue", outline="black"
        )

        # tb1 카메라 이미지를 표시할 라벨
        self.camera_label_tb1 = Label(root)
        self.camera_label_tb1.grid(row=0, column=1)

        # tb2 카메라 이미지를 표시할 라벨
        self.camera_label_tb2 = Label(root)
        self.camera_label_tb2.grid(row=0, column=2)

    def load_map_data(self, map_file):
        """YAML 파일에서 맵 데이터를 로드하는 함수"""
        with open(map_file, 'r') as file:
            map_data = yaml.safe_load(file)
        
        map_path = Path(map_file).parent / map_data['image']
        map_data['image'] = str(map_path)  # 상대 경로를 절대 경로로 변경

        return map_data

    def update_robot_position(self, x, y, orientation, robot='tb2'):
        """로봇의 위치를 맵에 업데이트하는 함수"""
        # 원점을 중앙으로 설정하고, 해상도를 고려하여 맵 상의 위치 계산
        canvas_x = (x - self.origin[0]) / self.resolution
        canvas_y = (y - self.origin[1]) / self.resolution

        # 맵 크기에 맞춰 비례적으로 위치 계산
        scale_x = 800 / self.map_width
        scale_y = 800 / self.map_height

        # 실제 맵 크기 비율을 고려하여 위치 조정
        canvas_x *= scale_x
        canvas_y *= scale_y

        # y 좌표 반전 (왼쪽 하단 -> 왼쪽 상단)
        canvas_y = 800 - canvas_y

        # 회전 각도 (라디안 단위)
        angle = 2*math.atan2(orientation[2], orientation[3])  # 쿼터니언을 각도로 변환
        

        # 삼각형 회전 (회전 행렬을 사용)
        # 각 꼭짓점 (상단, 왼쪽 하단, 오른쪽 하단)
        vertices = [
            (canvas_x, canvas_y - 10),  # 상단
            (canvas_x - 10, canvas_y + 10),  # 왼쪽 하단
            (canvas_x + 10, canvas_y + 10)   # 오른쪽 하단
        ]

        rotated_vertices = []
        for (vx, vy) in vertices:
            # 회전 행렬을 사용하여 각 꼭짓점 회전
            rotated_x = (vx - canvas_x) * math.cos(angle) - (vy - canvas_y) * math.sin(angle) + canvas_x
            rotated_y = (vx - canvas_x) * math.sin(angle) + (vy - canvas_y) * math.cos(angle) + canvas_y
            rotated_vertices.append((rotated_x, rotated_y))

        # 삼각형 위치 업데이트
        if robot == 'tb2':
            self.canvas.coords(self.robot_triangle_tb2, *rotated_vertices[0], *rotated_vertices[1], *rotated_vertices[2])
        elif robot == 'tb1':
            self.canvas.coords(self.robot_triangle_tb1, *rotated_vertices[0], *rotated_vertices[1], *rotated_vertices[2])


        # # 로봇 점 위치 업데이트
        # if robot == 'tb2':
        #     # self.canvas.coords(self.robot_dot_tb2, canvas_x - 5, canvas_y - 5, canvas_x + 5, canvas_y + 5)
        #     self.canvas.coords(
        #         self.robot_triangle_tb2,
        #         canvas_x, canvas_y - 10,  # 상단 꼭짓점
        #         canvas_x - 10, canvas_y + 10,  # 왼쪽 하단
        #         canvas_x + 10, canvas_y + 10   # 오른쪽 하단
        #     )
        # elif robot == 'tb1':
        #     # self.canvas.coords(self.robot_dot_tb1, canvas_x - 5, canvas_y - 5, canvas_x + 5, canvas_y + 5)
        #     self.canvas.coords(
        #         self.robot_triangle_tb1,
        #         canvas_x, canvas_y - 10,  # 상단 꼭짓점
        #         canvas_x - 10, canvas_y + 10,  # 왼쪽 하단
        #         canvas_x + 10, canvas_y + 10   # 오른쪽 하단
        #     )

    def update_tb1_camera_image(self, pil_image):
        """카메라 이미지를 Tkinter 라벨에 업데이트하는 함수"""
        pil_image = pil_image.resize((400, 400))  # 카메라 이미지를 라벨 크기에 맞게 리사이즈
        camera_photo = ImageTk.PhotoImage(pil_image)
        self.camera_label_tb1.config(image=camera_photo)
        self.camera_label_tb1.image = camera_photo  # 이미지를 라벨에 할당하여 계속 갱신되도록 합니다.

    def update_tb2_camera_image(self, pil_image):
        """카메라 이미지를 Tkinter 라벨에 업데이트하는 함수"""
        pil_image = pil_image.resize((400, 400))  # 카메라 이미지를 라벨 크기에 맞게 리사이즈
        camera_photo = ImageTk.PhotoImage(pil_image)
        self.camera_label_tb2.config(image=camera_photo)
        self.camera_label_tb2.image = camera_photo  # 이미지를 라벨에 할당하여 계속 갱신되도록 합니다.



def main(args=None):
    rclpy.init(args=args)

    # Tkinter 애플리케이션 생성
    root = Tk()
    root.title("Control Tower")

    # map.yaml 파일 경로
    map_file = '/home/bok/map.yaml'  # 실제 map.yaml 경로로 수정

    # 맵 해상도 및 원점 값
    resolution = 0.07  # m/픽셀
    origin = [-6.32, -6.87, 0]  # 맵 원점 (x, y)

    # Tkinter 기반 맵 뷰어 생성
    map_viewer = MapViewer(root, map_file, resolution, origin)

    # ROS 2 노드 생성
    odom_node = OdomNode(map_viewer)

    # 주기적으로 tkinter 윈도우 업데이트
    def update_gui():
        # 실시간으로 좌표를 tkinter 맵에 업데이트
        map_viewer.update_robot_position(odom_node.x_tb2, odom_node.y_tb2, (odom_node.x_tb2_quat, odom_node.y_tb2_quat, odom_node.z_tb2_quat, odom_node.w_tb2_quat), robot='tb2')
        map_viewer.update_robot_position(odom_node.x_tb1, odom_node.y_tb1, (odom_node.x_tb1_quat, odom_node.y_tb1_quat, odom_node.z_tb1_quat, odom_node.w_tb1_quat), robot='tb1')
        root.after(100, update_gui)  # 100ms마다 갱신

    # ROS 2 노드를 spin하여 메시지 처리
    def ros_spin():
        rclpy.spin(odom_node)

    # ROS spin을 별도의 스레드에서 실행
    ros_thread = threading.Thread(target=ros_spin)
    ros_thread.daemon = True
    ros_thread.start()

    # Tkinter GUI 실행
    update_gui()
    root.mainloop()


if __name__ == '__main__':
    main()

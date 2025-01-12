import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose, Point
from std_msgs.msg import Int32
from gazebo_msgs.srv import SpawnEntity
import random
import os

class ThiefSpawn(Node):
    def __init__(self):
        super().__init__('thief_spawn')
        
        self.get_logger().info("가제보 실행 대기중")
        self.spawn_service = self.create_client(SpawnEntity, '/spawn_entity')
        self.spawn_service.wait_for_service()
        
        self.coordinates = [
            (3.26, 4.75, 0.5),
            (-4.75, 0.605, 0.5),
            (-0.318, -5.31, 0.5),
            (-2.7, -3.07, 0.5),
            (-0.516, 0.665, 0.5),
        ]   

        self.thief_point_publisher = self.create_publisher(
            Point, 
            '/thief_point',
            10)
        
        self.spawn_random_object()
    
    def spawn_random_object(self):
        self.spawned_coordinates = random.choice(self.coordinates)
        x, y, z = self.spawned_coordinates
    
        sdf_file_path = os.path.join(
            os.getenv('HOME'), 
            'person_walking', 
            'model.sdf'
        )
    
        if not os.path.exists(sdf_file_path):
            self.get_logger().error(f"모델링을 읽어올 수 없음: {sdf_file_path}")
            return
    
        with open(sdf_file_path, 'r') as sdf_file:
            sdf_data = sdf_file.read()
        
        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z

        request = SpawnEntity.Request()
        request.name = 'thief_spawn'
        request.xml = sdf_data
        request.robot_namespace = ''
        request.initial_pose = pose

        self.get_logger().info(f"도둑 생성 대기중: ({x}, {y}, {z})")
        future = self.spawn_service.call_async(request)
        future.add_done_callback(self.spawn_response_callback)
        
    def publish_thief_coordinates(self):
        msg = Point()
        msg.x, msg.y, msg.z = self.spawned_coordinates
        self.thief_point_publisher.publish(msg)
        self.get_logger().info(f"도둑 좌표 발행 완료: ({msg.x}, {msg.y}, {msg.z})")
        
    def thief_spawn_topic(self):
        self.publisher_ = self.create_publisher(Int32, 'thief_spawn', 10)
        msg = Int32()
        msg.data = 1
        self.publisher_.publish(msg)
        self.get_logger().info('토픽 발행 완료')
        
    def spawn_response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info("도둑 등장!")
            self.thief_spawn_topic()
            self.publish_thief_coordinates()  # 좌표 발행
        except Exception as e:
            self.get_logger().error(f"도둑 생성 실패 : {e}")

def main(args=None):
    rclpy.init(args=args)
    node = ThiefSpawn()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

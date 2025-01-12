import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Pose
import time, ikpy

class RobotArmControl(Node):
    def __init__(self):
        super().__init__('robot_arm_control')

        # 목표 위치 (target_position)
        self.target_position = [0.1, 0.1, 0.1]

        # ROS 퍼블리셔 설정 (관절 위치 제어)
        self.joint_publisher = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)

    def move_to_target(self, target_position):
        my_chain = ikpy.chain.Chain.from_urdf_file("openmanipulator_sub.URDF")
        # 역기구학을 통해 관절 각도 계산
        joint_angles = my_chain.inverse_kinematics(target_position)
        
        # JointTrajectory 메시지 생성
        joint_trajectory = JointTrajectory()
        joint_trajectory.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4"]  # 관절 이름 설정
        joint_trajectory.points = [JointTrajectoryPoint(positions=joint_angles, time_from_start=rclpy.duration.Duration(seconds=2))]

        # 퍼블리셔를 통해 관절 제어 명령 전송
        self.joint_publisher.publish(joint_trajectory)
        self.get_logger().info(f"Moving to target: {target_position}")

    def stop(self):
        # 로봇 팔 멈추기
        joint_trajectory = JointTrajectory()
        joint_trajectory.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4"]
        joint_trajectory.points = [JointTrajectoryPoint(positions=[0, 0, 0, 0], time_from_start=rclpy.duration.Duration(seconds=1))]
        self.joint_publisher.publish(joint_trajectory)
        self.get_logger().info("Stopping robot arm")

def main(args=None):
    rclpy.init(args=args)
    robot_control = RobotArmControl()

    # 목표 위치로 이동
    robot_control.move_to_target(robot_control.target_position)

    # 잠시 대기
    time.sleep(2)

    # 로봇 팔 멈추기
    robot_control.stop()

    rclpy.spin(robot_control)

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
from rclpy.action import ActionClient
from control_msgs.action import GripperCommand
import math
import time

# 로봇 팔의 링크 길이
r1 = 130  # J0 -> J1
r2 = 124  # J1 -> J2
r3 = 126  # J0 -> J2

# inverse kinematics 오프셋
th1_offset = -math.atan2(0.024, 0.128)
th2_offset = -0.5 * math.pi - th1_offset

# 두 점 사이의 각도를 구하는 함수
def solv2(r1, r2, r3):
    d1 = (r3**2 - r2**2 + r1**2) / (2 * r3)
    d2 = (r3**2 + r2**2 - r1**2) / (2 * r3)

    s1 = math.acos(d1 / r1)
    s2 = math.acos(d2 / r2)

    return s1, s2

# 목표 좌표 (x, y, z)에 대해 로봇 팔의 각도 계산
def solv_robot_arm2(x, y, z, r1, r2, r3):
    Rt = math.sqrt(x**2 + y**2 + z**2)
    Rxy = math.sqrt(x**2 + y**2)
    St = math.asin(z / Rt)
    #   Sxy = math.acos(x / Rxy)
    Sxy = math.atan2(y, x)

    s1, s2 = solv2(r1, r2, Rt)

    sr1 = math.pi/2 - (s1 + St)
    sr2 = s1 + s2
    sr2_ = sr1 + sr2
    sr3 = math.pi - sr2_

    J0 = (0, 0, 0)
    J1 = (J0[0] + r1 * math.sin(sr1)  * math.cos(Sxy),
            J0[1] + r1 * math.sin(sr1)  * math.sin(Sxy),
            J0[2] + r1 * math.cos(sr1))
    J2 = (J1[0] + r2 * math.sin(sr1 + sr2) * math.cos(Sxy),
            J1[1] + r2 * math.sin(sr1 + sr2) * math.sin(Sxy),
            J1[2] + r2 * math.cos(sr1 + sr2))
    J3 = (J2[0] + r3 * math.sin(sr1 + sr2 + sr3) * math.cos(Sxy),
            J2[1] + r3 * math.sin(sr1 + sr2 + sr3) * math.sin(Sxy),
            J2[2] + r3 * math.cos(sr1 + sr2 + sr3))
    
    return J0, J1, J2, J3, Sxy, sr1, sr2, sr3, St, Rt

class RobotArmControlNode(Node):
    def __init__(self):
        super().__init__('robot_arm_control')

        self.joint_pub = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        self.gripper_action_client = ActionClient(self, GripperCommand, 'gripper_controller/gripper_cmd')
        self.send_gripper_goal(0.025)

    def move_arm_to_position(self, x, y, z):
        # inverse kinematics 계산
        J0, J1, J2, J3, Sxy, sr1, sr2, sr3, St, Rt = solv_robot_arm2(x, y, z, r1, r2, r3)

        # JointTrajectory 메시지 생성
        self.trajectory_msg = JointTrajectory()
        self.trajectory_msg.header = Header()
        self.trajectory_msg.header.frame_id = 'base_link'  # 로봇의 기준 좌표계

        # 조인트 이름
        self.trajectory_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']

        # JointTrajectoryPoint 생성
        point = JointTrajectoryPoint()
        point.positions = [Sxy, sr1 + th1_offset, sr2 + th2_offset, sr3]
        point.velocities = [0.0] * 4
        point.time_from_start.sec = 1
        point.time_from_start.nanosec = 5000

        # 메시지에 조인트 포인트 추가
        self.trajectory_msg.points = [point]

        # 목표 위치로 로봇 팔을 이동
        self.joint_pub.publish(self.trajectory_msg)
        self.get_logger().info('Publishing joint trajectory: %s' % self.trajectory_msg)
        time.sleep(3)


    def send_gripper_goal(self, position):
        # 그리퍼 목표 설정
        goal = GripperCommand.Goal()
        goal.command.position = position
        goal.command.max_effort = -1.0

        if not self.gripper_action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().error("Gripper action server not available!")
            return

        self.gripper_action_client.send_goal_async(goal)

    def operate_gripper_and_move_arm(self, x, y, z):
        # 먼저 그리퍼를 열기
        self.send_gripper_goal(0.025)  # 그리퍼 열기
        self.get_logger().info('Opening gripper')
        
        # 기다리기
        time.sleep(1)

        # 로봇 팔을 목표 위치로 이동
        self.move_arm_to_position(x, y, z)
        
        # 기다리기
        time.sleep(3)

        # 목표 위치에 도달 후 그리퍼를 닫기
        self.send_gripper_goal(-0.15)  # 그리퍼 닫기
        time.sleep(2)
        self.get_logger().info('Closing gripper')
       
        # 기다리기
        time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    node = RobotArmControlNode()
    '''
    node.send_gripper_goal(0.025)
    time.sleep(2)
    node.move_arm_to_position(0,150,200)
    time.sleep(2)
    node.move_arm_to_position(0,190,140)
    time.sleep(2)
    node.send_gripper_goal(-0.15)
    time.sleep(2)
    node.trajectory_msg.points[0].positions[0]+=0.2
    node.joint_pub.publish(node.trajectory_msg)
    time.sleep(2)
    node.move_arm_to_position(0,40,230)
    time.sleep(2)
    node.move_arm_to_position(0,-40,230)'''

    node.move_arm_to_position(0,-210,140)
    time.sleep(2)
    node.send_gripper_goal(0.025)
    time.sleep(2)
    node.mani_home()
    time.sleep(2)

if __name__ == '__main__':
    main()

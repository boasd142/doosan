#!/usr/bin/env python 
# Set linear and angular values of Turtlesim's speed and turning. 

import getkey
import rclpy	# Needed to create a ROS node 
from rclpy.action import ActionClient
from geometry_msgs.msg import Twist    # Message that moves base
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
from control_msgs.action import GripperCommand
from rclpy.node import Node
import math


r1 = 130
r2 = 124
r3 = 126


th1_offset = - math.atan2(0.024, 0.128)
th2_offset = - 0.5*math.pi - th1_offset

# author : karl.kwon (mrthinks@gmail.com)
# r1 : distance J0 to J1
# r2 : distance J1 to J2
# r3 : distance J0 to J2
def solv2(r1, r2, r3):
  d1 = (r3**2 - r2**2 + r1**2) / (2*r3)
  d2 = (r3**2 + r2**2 - r1**2) / (2*r3)

  s1 = math.acos(d1 / r1)
  s2 = math.acos(d2 / r2)

  return s1, s2

# author : karl.kwon (mrthinks@gmail.com)
# x, y, z : relational position from J0 (joint 0)
# r1 : distance J0 to J1
# r2 : distance J1 to J2
# r3 : distance J2 to J3
# sr1 : angle between z-axis to J0->J1
# sr2 : angle between J0->J1 to J1->J2
# sr3 : angle between J1->J2 to J2->J3 (maybe always parallel)
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


usage = """
Control Your OpenManipulator!
---------------------------
Joint Space Control:
- Joint1 : Increase (Y), Decrease (H)
- Joint2 : Increase (U), Decrease (J)
- Joint3 : Increase (I), Decrease (K)
- Joint4 : Increase (O), Decrease (L)

INIT : (1)

CTRL-C to quit
"""

joint_angle_delta = 0.1  # radian

class Turtlebot3ManipulationTest(Node): 
    # settings = None
    # if os.name != 'nt':
    #     settings = termios.tcgetattr(sys.stdin)
    def __init__(self): 
        super().__init__('turtlebot3_manipulation_test')
        key_value = ''

        self.cmd_vel = self.create_publisher(Twist, '/cmd_vel', 10)
        self.joint_pub = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        self.gripper_action_client = ActionClient(self, GripperCommand, 'gripper_controller/gripper_cmd')
    
        self.move_cmd = Twist() 
        # Linear speed in x in meters/second is + (forward) or 
        #    - (backwards) 
        self.move_cmd.linear.x = 1.3   # Modify this value to change speed 
        # Turn at 0 radians/s 
        self.move_cmd.angular.z = 0.8 
        # Modify this value to cause rotation rad/s 

        self.trajectory_msg = JointTrajectory()

        J0, J1, J2, J3, Sxy, sr1, sr2, sr3, St, Rt = solv_robot_arm2(100, 0, 100, r1, r2, r3)

        self.trajectory_msg.header = Header()
        self.trajectory_msg.header.frame_id = ''
        self.trajectory_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']

        point = JointTrajectoryPoint()
        # point.positions = [0.003, math.pi / 4.0, -0.489, 2.041]
        # point.positions = [0.0] * 4
        point.positions = [Sxy, sr1 + th1_offset, sr2 + th2_offset, sr3]
        point.velocities = [0.0] * 4
        point.time_from_start.sec = 1
        point.time_from_start.nanosec = 5000

        self.trajectory_msg.points = [point]

        self.joint_pub.publish(self.trajectory_msg)

    # def timer_callback(self):
    #     print('.')
    #     self.joint_pub.publish(self.trajectory_msg)
    #     self.cmd_vel.publish(self.move_cmd) 
    def send_gripper_goal(self, position):
        # 그리퍼 목표 설정
        goal = GripperCommand.Goal()
        goal.command.position = position
        goal.command.max_effort = -1.0

        if not self.gripper_action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().error("Gripper action server not available!")
            return

        self.gripper_action_client.send_goal_async(goal)


node = None

def main(args=None):
    # rclpy.init(args=args)

    try:
        rclpy.init()
    except Exception as e:
        print(e)

    try:
        node = Turtlebot3ManipulationTest()
    except Exception as e:
        print(e)

    ''' 컨베이어에 다 넣고 돌아왔을때
    - joint1
    - joint2
    - joint3
    - joint4
    points:
    - positions:
    - 1.5708
    - -1.4454028293433383
    - 0.8759760016517062
    - 1.0402231544865281
    
    잡을때 위치
    - joint1
    - joint2
    - joint3
    - joint4
    points:
    - positions:
    - 1.5707963267948966
    - 0.5545980000000001
    - -0.7240239983482937
    - 1.5402231544865286

     잡은 이후
    - positions:
    - 1.5707963267948966
    - -0.44540199999999985
    - -0.12402399834829375
    - 1.5402231544865286

'''
    '''1번 구역
    0.20000000000000004
  - 0.45459717065666194
  - 0.2759760016517062
  - 0.44022315448652827


   2번
    - -0.4
    - 0.3545980000000002
    - 0.3759760016517063
    - 0.5402231544865282
    3번
    - 0.19999999999999998
    - 0.7545980000000001
    - -0.42402399834829374
    - 0.9402231544865282
    4번
    - -0.30000000000000004
  - 0.7545980000000001
  - -0.42402399834829374
  - 0.8402231544865282

    red, blue박스 놓을때
    - 1.3
    - 0.8545971706566619
    - -0.9240239983482937
    - 1.2402231544865283

'''

    try:
        while(rclpy.ok()):
            # rclpy.spin_once(node)
            key_value = getkey.getkey()
            if key_value == 'z':
                node.send_gripper_goal(0.025)

            if key_value == 'x':
                node.send_gripper_goal(-0.15)

            if key_value == '0':
                node.trajectory_msg.points[0].positions[0] = 0
                node.trajectory_msg.points[0].positions[1] = -1.445402
                node.trajectory_msg.points[0].positions[2] = 0.8759760016517062
                node.trajectory_msg.points[0].positions[3] = 1.1402231544865281
                node.joint_pub.publish(node.trajectory_msg)

            if key_value == '1':
                node.trajectory_msg.points[0].positions[0] = math.pi/2
                node.trajectory_msg.points[0].positions[1] = -1.445402
                node.trajectory_msg.points[0].positions[2] = 0.8759760016517062
                node.trajectory_msg.points[0].positions[3] = 1.0402231544865281
                node.joint_pub.publish(node.trajectory_msg)
            
            if key_value == '2':
                node.trajectory_msg.points[0].positions[0] = 1.5707963267948966
                node.trajectory_msg.points[0].positions[1] = 0.5545980000000001
                node.trajectory_msg.points[0].positions[2] = -0.7240239983482937
                node.trajectory_msg.points[0].positions[3] = 1.5402231544865286
                node.joint_pub.publish(node.trajectory_msg)
            
            if key_value == '3':
                node.trajectory_msg.points[0].positions[0] = 1.5707963267948966
                node.trajectory_msg.points[0].positions[1] = -0.44540199999999985
                node.trajectory_msg.points[0].positions[2] = -0.12402399834829375
                node.trajectory_msg.points[0].positions[3] = 1.5402231544865286
                node.joint_pub.publish(node.trajectory_msg)

            if key_value == '4':
                node.trajectory_msg.points[0].positions[0] = 1.5707963267948966 + math.pi
                node.trajectory_msg.points[0].positions[1] = -0.44540199999999985
                node.trajectory_msg.points[0].positions[2] = -0.12402399834829375
                node.trajectory_msg.points[0].positions[3] = 1.5402231544865286
                node.joint_pub.publish(node.trajectory_msg)
            
            if key_value == '5':
                node.trajectory_msg.points[0].positions[0] = -1.5707963267948966
                node.trajectory_msg.points[0].positions[1] = 0.45459800000000017
                node.trajectory_msg.points[0].positions[2] = -0.8240239983482937
                node.trajectory_msg.points[0].positions[3] = 1.2402231544865283
                node.joint_pub.publish(node.trajectory_msg)
            
            if key_value == 'a':
                node.trajectory_msg.points[0].positions[0] = 0.20000000000000004
                node.trajectory_msg.points[0].positions[1] = 0.45459717065666194
                node.trajectory_msg.points[0].positions[2] = 0.2759760016517062
                node.trajectory_msg.points[0].positions[3] = 0.44022315448652827
                node.joint_pub.publish(node.trajectory_msg)
                
            if key_value == 's':
                node.trajectory_msg.points[0].positions[0] = -0.4      
                node.trajectory_msg.points[0].positions[1] = 0.3545980000000002
                node.trajectory_msg.points[0].positions[2] = 0.3759760016517063
                node.trajectory_msg.points[0].positions[3] = 0.5402231544865282
                node.joint_pub.publish(node.trajectory_msg)

            if key_value == 'd':
                node.trajectory_msg.points[0].positions[0] = 0.19999999999999998
                node.trajectory_msg.points[0].positions[1] = 0.7545980000000001
                node.trajectory_msg.points[0].positions[2] = -0.42402399834829374
                node.trajectory_msg.points[0].positions[3] = 0.9402231544865282
                node.joint_pub.publish(node.trajectory_msg)

            if key_value == 'f':
                node.trajectory_msg.points[0].positions[0] = -0.30000000000000004
                node.trajectory_msg.points[0].positions[1] = 0.7545980000000001
                node.trajectory_msg.points[0].positions[2] = -0.42402399834829374
                node.trajectory_msg.points[0].positions[3] =  0.8402231544865282
                node.joint_pub.publish(node.trajectory_msg)

            if key_value == 'g':
                node.trajectory_msg.points[0].positions[0] = 1.3
                node.trajectory_msg.points[0].positions[1] = 0.8545971706566619
                node.trajectory_msg.points[0].positions[2] = -0.9240239983482937
                node.trajectory_msg.points[0].positions[3] =  1.2402231544865283
                node.joint_pub.publish(node.trajectory_msg)



            elif key_value == 'y':
                node.trajectory_msg.points[0].positions[0] += joint_angle_delta
                node.joint_pub.publish(node.trajectory_msg)
                print('joint1 +')
            elif key_value == 'h':
                node.trajectory_msg.points[0].positions[0] -= joint_angle_delta
                node.joint_pub.publish(node.trajectory_msg)
                print('joint1 -')
            elif key_value == 'u':
                node.trajectory_msg.points[0].positions[1] += joint_angle_delta
                node.joint_pub.publish(node.trajectory_msg)
                print('joint2 +')
            elif key_value == 'j':
                node.trajectory_msg.points[0].positions[1] -= joint_angle_delta
                node.joint_pub.publish(node.trajectory_msg)
                print('joint2 -')
            elif key_value == 'i':
                node.trajectory_msg.points[0].positions[2] += joint_angle_delta
                node.joint_pub.publish(node.trajectory_msg)
                print('joint3 +')
            elif key_value == 'k':
                node.trajectory_msg.points[0].positions[2] -= joint_angle_delta
                node.joint_pub.publish(node.trajectory_msg)
                print('joint3 -')
            elif key_value == 'o':
                node.trajectory_msg.points[0].positions[3] += joint_angle_delta
                node.joint_pub.publish(node.trajectory_msg)
                print('joint4 +')
            elif key_value == 'l':
                node.trajectory_msg.points[0].positions[3] -= joint_angle_delta
                node.joint_pub.publish(node.trajectory_msg)
                print('joint4 -')
            elif key_value == 'q':
                break
            

    except Exception as e:
        print(e)

    finally:
        # if os.name != 'nt':
        #     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()


if __name__== "__main__": 
	main() 
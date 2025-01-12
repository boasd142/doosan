import os
import sys
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 각 테이블에 대한 메뉴 GUI 실행 노드 추가
        Node(
            package='turtlebot',  # 패키지 이름
            executable='menu1_gui',  # 실행할 스크립트 이름
            name='menu_gui_table_1',  # 노드 이름
            output='screen',
            parameters=[{'table_num': 1}]  # 테이블 번호 전달
        ),
        Node(
            package='turtlebot',  # 패키지 이름
            executable='menu2_gui',  # 실행할 스크립트 이름
            name='menu_gui_table_2',  # 노드 이름
            output='screen',
            parameters=[{'table_num': 2}]  # 테이블 번호 전달
        ),
        # 같은 방식으로 테이블 3부터 9까지 추가
        Node(
            package='turtlebot',
            executable='menu3_gui',
            name='menu_gui_table_3',
            output='screen',
            parameters=[{'table_num': 3}]
        ),
        Node(
            package='turtlebot',
            executable='menu4_gui',
            name='menu_gui_table_4',
            output='screen',
            parameters=[{'table_num': 4}]
        ),
        Node(
            package='turtlebot',
            executable='menu5_gui',
            name='menu_gui_table_5',
            output='screen',
            parameters=[{'table_num': 5}]
        ),
        Node(
            package='turtlebot',
            executable='menu6_gui',
            name='menu_gui_table_6',
            output='screen',
            parameters=[{'table_num': 6}]
        ),
        Node(
            package='turtlebot',
            executable='menu7_gui',
            name='menu_gui_table_7',
            output='screen',
            parameters=[{'table_num': 7}]
        ),
        Node(
            package='turtlebot',
            executable='menu8_gui',
            name='menu_gui_table_8',
            output='screen',
            parameters=[{'table_num': 8}]
        ),
        Node(
            package='turtlebot',
            executable='menu9_gui',
            name='menu_gui_table_9',
            output='screen',
            parameters=[{'table_num': 9}]
        ),
    ])

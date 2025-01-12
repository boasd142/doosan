from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='project',
            executable='control_tower',
            name='control_tower',
            output='screen'
        ),
        Node(
            package='project',
            executable='mani_control',
            name='mani_control',
            output='screen'
        ),
        Node(
            package='project',
            executable='fix_rotation',
            name='fix_rotation',
            output='screen'
        ),
    ])

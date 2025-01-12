from setuptools import find_packages, setup

package_name = 'turtlebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/menu_gui_launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bok',
    maintainer_email='bok@todo.todo',
    description='Turtlebot package for various functionalities.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle3_gui = turtlebot_gui.turtlebot_gui:main',
            'turtle3_gui2 = turtlebot_gui.turtlebot_gui2:main',
            'send_goal = turtlebot.send_goal:main',
            'pub_topic = turtlebot.pub_topic:main',
            'sub_topic = turtlebot.sub_topic:main',
            'menu2_gui = turtlebot.menu2_gui:main',  # menu_gui 엔트리 포인트
            'menu_sub = turtlebot.menu_sub:main',
            'order_list = turtlebot.order_list:main',
            'robot_gui = turtlebot.robot_gui:main',
            'menu1_gui = turtlebot.menu1_gui:main',
            'menu3_gui = turtlebot.menu3_gui:main',
            'menu4_gui = turtlebot.menu4_gui:main',
            'menu5_gui = turtlebot.menu5_gui:main',
            'menu6_gui = turtlebot.menu6_gui:main',
            'menu7_gui = turtlebot.menu7_gui:main',
            'menu8_gui = turtlebot.menu8_gui:main',
            'menu9_gui = turtlebot.menu9_gui:main',
            'menu_gui = turtlebot.menu_gui:main',
            'turtlebot3_gui3 = turtlebot.turtlebot3_gui3:main',
        ],
    },
)

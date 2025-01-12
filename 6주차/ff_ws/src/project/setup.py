from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # launch 파일 추가
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bok',
    maintainer_email='sorkaksema@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control_tower=project.control_tower:main',
            'server=project.control_tower_server:main',
            'camera=project.camera:main',
            'mani_control=project.subscription:main',
            'fix_rotation=project.fix_rotation:main',
        ],
    },
)

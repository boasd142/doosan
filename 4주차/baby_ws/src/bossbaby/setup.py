from setuptools import find_packages, setup

package_name = 'bossbaby'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bok',
    maintainer_email='sorkaksema@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    #tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	"app=bossbaby.app:main",
        	"subscriber=bossbaby.subscriber:main",
            "detection=bossbaby.detection:main",
            "up_flask=bossbaby.up_flask:main",
            "up_camera=bossbaby.up_camera:main",
            "move=bossbaby.move:main",
            "move_test=bossbaby.move_test:main",
        ],	
    },
)

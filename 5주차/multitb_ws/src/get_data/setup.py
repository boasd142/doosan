from setuptools import find_packages, setup

package_name = 'get_data'

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
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'get_data=get_data.get_data:main',
            'qt_update=get_data.qt_update:main',
            'thief_spawn=get_data.thief_spawn:main',
            'camera=get_data.camera:main',
        ],
    },
)

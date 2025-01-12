from setuptools import find_packages
from setuptools import setup

setup(
    name='order_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('order_msgs', 'order_msgs.*')),
)

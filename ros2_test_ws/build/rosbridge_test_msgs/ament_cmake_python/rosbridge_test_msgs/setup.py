from setuptools import find_packages
from setuptools import setup

setup(
    name='rosbridge_test_msgs',
    version='2.1.0',
    packages=find_packages(
        include=('rosbridge_test_msgs', 'rosbridge_test_msgs.*')),
)

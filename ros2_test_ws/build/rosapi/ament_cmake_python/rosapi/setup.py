from setuptools import find_packages
from setuptools import setup

setup(
    name='rosapi',
    version='2.1.0',
    packages=find_packages(
        include=('rosapi', 'rosapi.*')),
)

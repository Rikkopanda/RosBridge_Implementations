#!/bin/bash

source ~/.bashrc

source ~/Documents/coding/CORE_CODAM/ft_transcendence_github/Test_Project_Seperate/RosBridge_Implementations/ros2_test_ws/install/setup.bash

ros2 run joy joy_node --ros-args -p rate:=1 -p dev:=/dev/input/js &

ros2 launch rosbridge_server rosbridge_websocket_launch.xml &

python3 manage.py runserver

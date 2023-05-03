#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import sys, os, rclpy, time
from std_msgs.msg import Int8, Float32
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.executors import MultiThreadedExecutor
from threading import Thread
from rclpy.qos import QoSProfile
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic


# UI 파일 연결
gui_formet = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'my_gui.ui'))

# 화면을 띄우는데 사용되는 Class 선언
class GUIWidget(QWidget, gui_formet[0], Node):

    def __init__(self):
        super(GUIWidget, self).__init__()
        self.setupUi(self)
        self.setObjectName('GUI')
        qos = QoSProfile(depth=10)

        self.speed = Float32()
        self.speed = 0.0  # 부동 소수점 값으로 초기화

        self.pub_velocity = Twist()
        self.pub_velocity.linear.x = 0.0
        self.pub_velocity.angular.z = 0.0
        self.pub_velocity.linear.z = 0.0

        # self.control_running = False
        # self.executor_ = MultiThreadedExecutor(num_threads=2)
        # self.executor_.add_node(self)

        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', qos)
        
        # self.high_speed_button.clicked.connect(self.speed_up_callback)
        # self.low_speed_button.clicked.connect(self.speed_down_callback)

        self.forward.clicked.connect(self.front_command_callback)
        self.left_button.clicked.connect(self.left_command_callback)
        self.right_button.clicked.connect(self.right_command_callback)
        self.rear_button.clicked.connect(self.rear_command_callback)
        self.spot_button.clicked.connect(self.stop_command_callback)
        

    # joystick control button
    def front_command_callback(self):
        self.pub_velocity.linear.x += self.speed.data
        print("forward, speed :", self.speed.data)
        self.cmd_pub.publish(self.pub_velocity)

    def left_command_callback(self):
        self.pub_velocity.angular.z += self.speed.data
        print("left_button, speed :", self.speed.data)
        self.cmd_pub.publish(self.pub_velocity)

    def right_command_callback(self):
        self.pub_velocity.angular.z -= self.speed.data
        print("right_button, speed :", self.speed.data)
        self.cmd_pub.publish(self.pub_velocity)

    def rear_command_callback(self):
        self.pub_velocity.linear.x -= self.speed.data
        print("back_button, speed :", self.speed.data)
        self.cmd_pub.publish(self.pub_velocity)

    def stop_command_callback(self):
        self.pub_velocity.linear.x = 0.0
        self.pub_velocity.angular.z = 0.0
        print("spot_button", self.speed.data)
        self.cmd_pub.publish(self.pub_velocity)

    def lift_turn_button(self):
        self.pub_velocity.linear.z = 1.0
        self.cmd_pub.publish(self.pub_velocity)
        print("lift_turn")

    def right_turn_button(self):
        self.pub_velocity.linear.z = -1.0
        self.cmd_pub.publish(self.pub_velocity)
        print("right_turn")

    # def spin(self):
    #     try:
    #         if not self.control_running(self):
    #             self.executor_.spin()
    #             time.sleep(0.01)
    #             Thread(target=self.spin).start()
    #     except KeyboardInterrupt:
    #         self.executor_.shutdown()

    def shutdown_widget(self):
        self.destroy_subscription(self.subscriber)
        self.destroy_publisher(self.publisher)

def main(args=None):
    rclpy.init(args=args)
    app = QApplication(sys.argv)
    node = rclpy.create_node('GUIWidget')
    widget = GUIWidget()
    widget.show()
    app.exec_()
    rclpy.spin(node)
    widget.shutdown_widget()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

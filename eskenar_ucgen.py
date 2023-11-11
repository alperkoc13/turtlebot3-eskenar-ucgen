#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:59:09 2023

@author: alper
"""

import rospy 
from geometry_msgs.msg import Twist
import math

rospy.init_node('draw_equilatera_triange')
pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
rospy.Rate(10)
kontrol=Twist()


uzunluk=2
donme=math.radians(37)

for _ in range(4):
    kontrol.linear.x=uzunluk
    kontrol.angular.z=0.0
    pub.publish(kontrol)
    rospy.sleep(uzunluk/2)
    
    kontrol.linear.x=0
    kontrol.angular.z=0.0
    pub.publish(kontrol)
    rospy.sleep(2)
    
    kontrol.linear.x=0.0
    kontrol.angular.z=donme
    pub.publish(kontrol)
    rospy.sleep(2)
    
    kontrol.linear.x=0
    kontrol.angular.z=0
    pub.publish(kontrol)
    rospy.sleep(2.5)
    
kontrol.linear.x=0.0
kontrol.angular.z=0.0
pub.publish(kontrol)






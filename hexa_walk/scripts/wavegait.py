#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def talker():
    pub1 = rospy.Publisher('/hexaurdf10/j_c1_rf_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/hexaurdf10/j_c1_rr_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/hexaurdf10/j_c1_lm_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/hexaurdf10/j_thigh_rf_position_controller/command', Float64, queue_size=10)
    pub5 = rospy.Publisher('/hexaurdf10/j_thigh_rr_position_controller/command', Float64, queue_size=10)
    pub6 = rospy.Publisher('/hexaurdf10/j_thigh_lm_position_controller/command', Float64, queue_size=10)
    pub7 = rospy.Publisher('/hexaurdf10/j_c1_rm_position_controller/command', Float64, queue_size=10)
    pub8 = rospy.Publisher('/hexaurdf10/j_c1_lr_position_controller/command', Float64, queue_size=10)
    pub9 = rospy.Publisher('/hexaurdf10/j_c1_lf_position_controller/command', Float64, queue_size=10)
    pub10 = rospy.Publisher('/hexaurdf10/j_thigh_rm_position_controller/command', Float64, queue_size=10)
    pub11 = rospy.Publisher('/hexaurdf10/j_thigh_lr_position_controller/command', Float64, queue_size=10)
    pub12 = rospy.Publisher('/hexaurdf10/j_thigh_lf_position_controller/command', Float64, queue_size=10)
    
    rospy.init_node('hexa_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    position = 0
    while not rospy.is_shutdown():
        for i1 in range(0,20):
            position = (i1*math.pi)/180
            rospy.loginfo(position)
            pub1.publish(position)
            pub4.publish(position)
            rospy.sleep(0.01)
        for j1 in range(20,-1,-1):
            position = (j1*math.pi)/180
            rospy.loginfo(position)
            pub4.publish(position)
            rospy.sleep(0.01)
        for i2 in range(0,20):
            position = (i2*math.pi)/180
            rospy.loginfo(position)
            pub7.publish(position)
            pub10.publish(position)
            rospy.sleep(0.01)
        for j2 in range(20,-1,-1):
            position = (j2*math.pi)/180
            rospy.loginfo(position)
            pub10.publish(position)
            rospy.sleep(0.01)
        for i3 in range(0,20):
            position = (i3*math.pi)/180
            rospy.loginfo(position)
            pub2.publish(position)
            pub5.publish(position)
            rospy.sleep(0.01)
        for j3 in range(20,-1,-1):
            position = (j3*math.pi)/180
            rospy.loginfo(position)
            pub5.publish(position)
            rospy.sleep(0.01)
        for i4 in range(0,20):
            position = (i4*math.pi)/180
            rospy.loginfo(position)
            pub9.publish(position)
            pub12.publish(position)
            rospy.sleep(0.01)
        for j4 in range(20,-1,-1):
            position = (j4*math.pi)/180
            rospy.loginfo(position)
            pub12.publish(position)
            rospy.sleep(0.01)
        for i5 in range(0,20):
            position = (i5*math.pi)/180
            rospy.loginfo(position)
            pub3.publish(position)
            pub6.publish(position)
            rospy.sleep(0.01)
        for j5 in range(20,-1,-1):
            position = (j5*math.pi)/180
            rospy.loginfo(position)
            pub6.publish(position)
            rospy.sleep(0.01)
        for i6 in range(0,20):
            position = (i6*math.pi)/180
            rospy.loginfo(position)
            pub8.publish(position)
            pub11.publish(position)
            rospy.sleep(0.01)
        for j6 in range(20,-1,-1):
            position = (j6*math.pi)/180
            rospy.loginfo(position)
            pub11.publish(position)
            rospy.sleep(0.01)
        for k0 in range(20,0,-1):
            position = (k0*math.pi)/180
            rospy.loginfo(position)
            pub1.publish(position)
            pub7.publish(position)
            pub2.publish(position)
            pub9.publish(position)
            pub3.publish(position)
            pub8.publish(position)
            rospy.sleep(0.01)

        

        
        
        
        
        
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

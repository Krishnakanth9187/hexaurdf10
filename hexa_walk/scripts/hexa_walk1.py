#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
from sensor_msgs.msg import Imu

def callback(data):
    global z
    x = data.orientation.x
    y = data.orientation.y
    z = data.orientation.z
    w = data.orientation.w
    print(x,y,z,w)
    return z
    
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
    imu_subscriber = rospy.Subscriber('/imu',Imu,callback)
    rospy.init_node('hexa_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    position = 0
    while not rospy.is_shutdown():
        if z >= 0.6:
            for i in range(0,20):
                position = (i*math.pi)/180
                rospy.loginfo(position)
                pub1.publish(position)
                pub2.publish(position)
                pub3.publish(position)
                rospy.sleep(0.01)
            for j in range(20,-2,-1):
                position = (j*math.pi)/180
                rospy.loginfo(position)
                pub4.publish(position)
                pub5.publish(position)
                pub6.publish(position)
                rospy.sleep(0.01)
            for o in range(0,20):
                position = (o*math.pi)/180
                rospy.loginfo(position)
                pub10.publish(position)
                pub11.publish(position)
                pub12.publish(position)
                rospy.sleep(0.01)
            for k in range(20,0,-1):
                position = (k*math.pi)/180
                rospy.loginfo(position)
                pub1.publish(position)
                pub2.publish(position)
                pub3.publish(position)
                rospy.sleep(0.01)
            for l in range(0,20):
                position = (l*math.pi)/180
                rospy.loginfo(position)
                pub7.publish(position)
                pub8.publish(position)
                pub9.publish(position)
                rospy.sleep(0.01)
            for m in range(20,-2,-1):
                position = (m*math.pi)/180
                rospy.loginfo(position)
                pub10.publish(position)
                pub11.publish(position)
                pub12.publish(position)
                rospy.sleep(0.01)
            for p in range(0,20):
                position = (p*math.pi)/180
                rospy.loginfo(position)
                pub4.publish(position)
                pub5.publish(position)
                pub6.publish(position)
                rospy.sleep(0.01)
            for n in range(20,0,-1):
                position = (n*math.pi)/180
                rospy.loginfo(position)
                pub7.publish(position)
                pub8.publish(position)
                pub9.publish(position)
                rospy.sleep(0.01)
        else:
            position = 0
            pub1.publish(position)
            pub2.publish(position)
            pub3.publish(position)
            pub4.publish(position)
            pub5.publish(position)
            pub6.publish(position)
            pub7.publish(position)
            pub8.publish(position)
            pub9.publish(position)
            pub10.publish(position)
            pub11.publish(position)
            pub12.publish(position)
            rospy.sleep(5)



        
        
        

if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
from sensor_msgs.msg import Imu
from gazebo_msgs.msg import ContactsState


class hexa_walking_control:
    def __init__(self):
        self.pub1 = rospy.Publisher('/hexaurdf10/j_c1_rf_position_controller/command', Float64, queue_size=10)
        self.pub2 = rospy.Publisher('/hexaurdf10/j_c1_rr_position_controller/command', Float64, queue_size=10)
        self.pub3 = rospy.Publisher('/hexaurdf10/j_c1_lm_position_controller/command', Float64, queue_size=10)
        self.pub4 = rospy.Publisher('/hexaurdf10/j_thigh_rf_position_controller/command', Float64, queue_size=10)
        self.pub5 = rospy.Publisher('/hexaurdf10/j_thigh_rr_position_controller/command', Float64, queue_size=10)
        self.pub6 = rospy.Publisher('/hexaurdf10/j_thigh_lm_position_controller/command', Float64, queue_size=10)
        self.pub7 = rospy.Publisher('/hexaurdf10/j_c1_rm_position_controller/command', Float64, queue_size=1)
        self.pub8 = rospy.Publisher('/hexaurdf10/j_c1_lr_position_controller/command', Float64, queue_size=10)
        self.pub9 = rospy.Publisher('/hexaurdf10/j_c1_lf_position_controller/command', Float64, queue_size=10)
        self.pub10 = rospy.Publisher('/hexaurdf10/j_thigh_rm_position_controller/command', Float64, queue_size=10)
        self.pub11 = rospy.Publisher('/hexaurdf10/j_thigh_lr_position_controller/command', Float64, queue_size=10)
        self.pub12 = rospy.Publisher('/hexaurdf10/j_thigh_lf_position_controller/command', Float64, queue_size=10)
        self.rate = rospy.Rate(100)
        self.imu_subscriber = rospy.Subscriber('/imu',Imu,self.walker)
        #self.tip1_subscriber = rospy.Subscriber('/tip1_contactsensor_state',ContactsState,self.walker)
        #self.tip2_subscriber = rospy.Subscriber('/tip2_contactsensor_state',ContactsState,self.walker)
        #self.tip3_subscriber = rospy.Subscriber('/tip3_contactsensor_state',ContactsState,self.walker)
        #self.tip4_subscriber = rospy.Subscriber('/tip4_contactsensor_state',ContactsState,self.walker)
        #self.tip5_subscriber = rospy.Subscriber('/tip5_contactsensor_state',ContactsState,self.walker)
        #self.tip6_subscriber = rospy.Subscriber('/tip6_contactsensor_state',ContactsState,self.walker)
        self.position = 0


    def walker(self,imu_subscriber):
        self.z = imu_subscriber.orientation.z*180/math.pi
        if self.z != 0:
            for i in range(0,20):
                self.position = (i*math.pi)/180
                rospy.loginfo(self.position)
                self.pub4.publish(self.position)
                self.pub5.publish(self.position)
                self.pub6.publish(self.position)
                rospy.sleep(0.01)
            for j in range(0,20):
                self.position = (j*math.pi)/180
                rospy.loginfo(self.position)
                self.pub1.publish(self.position)
                self.pub2.publish(self.position)
                self.pub3.publish(self.position)
                rospy.sleep(0.01)
            for o in range(20,0,-1):
                self.position = (o*math.pi)/180
                rospy.loginfo(self.position)
                self.pub4.publish(self.position)
                self.pub5.publish(self.position)
                self.pub6.publish(self.position)
                rospy.sleep(0.01)
            for k in range(0,20):
                self.position = (k*math.pi)/180
                rospy.loginfo(self.position)
                self.pub10.publish(self.position)
                self.pub11.publish(self.position)
                self.pub12.publish(self.position)
                rospy.sleep(0.01)
            for l in range(20,0,-1):
                self.position = (l*math.pi)/180
                rospy.loginfo(self.position)
                self.pub1.publish(self.position)
                self.pub2.publish(self.position)
                self.pub3.publish(self.position)
                rospy.sleep(0.01)
            for m in range(0,20):
                self.position = (m*math.pi)/180
                rospy.loginfo(self.position)
                self.pub7.publish(self.position)
                self.pub8.publish(self.position)
                self.pub9.publish(self.position)
                rospy.sleep(0.01)
            for p in range(20,0,-1):
                self.position = (p*math.pi)/180
                rospy.loginfo(self.position)
                self.pub10.publish(self.position)
                self.pub11.publish(self.position)
                self.pub12.publish(self.position)
                rospy.sleep(0.01)
            for n in range(0,20):
                self.position = (n*math.pi)/180
                rospy.loginfo(self.position)
                self.pub4.publish(self.position)
                self.pub5.publish(self.position)
                self.pub6.publish(self.position)
                rospy.sleep(0.01)
        #else:
            #print("inside else z = ",self.z)
            #self.position = 0
            #self.pub1.publish(self.position)
            #self.pub2.publish(self.position)
            #self.pub3.publish(self.position)
            #self.pub4.publish(self.position)
            #self.pub5.publish(self.position)
            #self.pub6.publish(self.position)
            #self.pub7.publish(self.position)
            #self.pub8.publish(self.position)
            #self.pub9.publish(self.position)
            #self.pub10.publish(self.position)
            #self.pub11.publish(self.position)
            #self.pub12.publish(self.position)
            #rospy.sleep(2)
            

    
    
    



        
        
        

if __name__ == '__main__':
    rospy.init_node('hexa_talker', anonymous=True)
    a= hexa_walking_control()
    rospy.spin()


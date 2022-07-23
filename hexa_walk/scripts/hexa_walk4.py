#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import message_filters
from sensor_msgs.msg import Imu
from gazebo_msgs.msg import ContactsState
from geometry_msgs.msg import Twist



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
        self.imu_subscriber = message_filters.Subscriber('/imu',Imu)
        self.tip1_subscriber = message_filters.Subscriber('/tip1_contactsensor_state',ContactsState)
        self.tip2_subscriber = message_filters.Subscriber('/tip2_contactsensor_state',ContactsState)
        self.tip3_subscriber = message_filters.Subscriber('/tip3_contactsensor_state',ContactsState)
        self.tip4_subscriber = message_filters.Subscriber('/tip4_contactsensor_state',ContactsState)
        self.tip5_subscriber = message_filters.Subscriber('/tip5_contactsensor_state',ContactsState)
        self.tip6_subscriber = message_filters.Subscriber('/tip6_contactsensor_state',ContactsState)
        ts = message_filters.TimeSynchronizer([self.imu_subscriber,self.tip1_subscriber,self.tip2_subscriber,self.tip3_subscriber,self.tip4_subscriber,self.tip5_subscriber,self.tip6_subscriber], 10)
        ts.registerCallback(self.walker)
        self.position = 0
        self.i = 0
        self.j = 0
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0
        self.c5 = 0
        self.c6 = 0
        self.retraction1 = True
        self.retraction2 = True
        self.retraction3 = True
 


    def walker(self,imu_subscriber,tip1_subscriber,tip2_subscriber,tip3_subscriber,tip4_subscriber,tip5_subscriber,tip6_subscriber):
        self.x = abs(imu_subscriber.orientation.x*180/math.pi)
        self.y = abs(imu_subscriber.orientation.y*180/math.pi)
        f1 = tip1_subscriber.states
        f2 = tip2_subscriber.states
        f3 = tip3_subscriber.states
        f4 = tip4_subscriber.states
        f5 = tip5_subscriber.states
        f6 = tip6_subscriber.states
        if len(f1) != 0:
            #print(len(f1[-1].contact_normals))
            #print(f1[-1].contact_normals[-1].z)
            self.c1 = f1[-1].contact_normals[-1].z
        else:
            self.c1 = 0
        if len(f2) != 0:
            #print(f2[-1].contact_normals[-1].z)
            self.c2 = f2[-1].contact_normals[-1].z
        else:
            self.c2 = 0
        if len(f3) != 0:
            #print(len(f3[-1].contact_normals))
            #print(f3[-1].contact_normals[-1].z)
            self.c3 = f3[-1].contact_normals[-1].z
        else:
            self.c3 = 0
        if len(f4) != 0:
            #print(len(f4[-1].contact_normals))
            #print(f4[-1].contact_normals[-1].z)
            self.c4 = f4[-1].contact_normals[-1].z
        else:
            self.c4 = 0
        if len(f5) != 0:
            #print(len(f5[-1].contact_normals))
            #print(f5[-1].contact_normals[-1].z)
            self.c5 = f5[-1].contact_normals[-1].z
        else:
            self.c5 = 0
        if len(f6) != 0:
            #print(len(f6[-1].contact_normals))
            #print(f6[-1].contact_normals[-1].z)
            self.c6 = f6[-1].contact_normals[-1].z
        else:
            self.c6 = 0
        
 
        #print(self.x,self.y)
        if  0 <= self.x <= 3 and self.retraction3 == True:
            if self.retraction2 == True:
                rospy.sleep(0.05)
                for i in range(0,20):
                    self.position = (i*math.pi)/180
                    #rospy.loginfo(self.position)
                    self.pub1.publish(self.position)
                    self.pub2.publish(self.position)
                    self.pub3.publish(self.position)
                    rospy.sleep(0.01)
                for j in range(20,0,-1):
                    self.position = (j*math.pi)/180
                    #rospy.loginfo(self.position)
                    self.pub4.publish(self.position)
                    self.pub5.publish(self.position)
                    self.pub6.publish(self.position)
                    rospy.sleep(0.01)
                for o in range(0,20):
                    self.position = (o*math.pi)/180
                    #rospy.loginfo(self.position)
                    self.pub10.publish(self.position)
                    self.pub11.publish(self.position)
                    self.pub12.publish(self.position)
                    rospy.sleep(0.01)
                self.retraction1 = False
                self.retraction2 = False
            if (self.c1 != 0 and self.c3 != 0) or (self.c1 != 0 and self.c5 != 0) or (self.c3 != 0 and self.c5 != 0):
                for k in range(20,0,-1):
                    self.position = (k*math.pi)/180
                    #rospy.loginfo(self.position)
                    self.pub1.publish(self.position)
                    self.pub2.publish(self.position)
                    self.pub3.publish(self.position)
                    rospy.sleep(0.01)
                self.retraction1 = True
                if self.retraction1 == True:
                    for l in range(0,20):
                        self.position = (l*math.pi)/180
                        #rospy.loginfo(self.position)
                        self.pub7.publish(self.position)
                        self.pub8.publish(self.position)
                        self.pub9.publish(self.position)
                        rospy.sleep(0.01)
                    for m in range(20,0,-1):
                        self.position = (m*math.pi)/180
                        #rospy.loginfo(self.position)
                        self.pub10.publish(self.position)
                        self.pub11.publish(self.position)
                        self.pub12.publish(self.position)
                        rospy.sleep(0.01)
                    for p in range(0,20):
                        self.position = (p*math.pi)/180
                        #rospy.loginfo(self.position)
                        self.pub4.publish(self.position)
                        self.pub5.publish(self.position)
                        self.pub6.publish(self.position)
                        rospy.sleep(0.01)
            if ((self.c2 != 0 and self.c4 != 0) or (self.c2 != 0 and self.c6 != 0) or (self.c4 != 0 and self.c6 != 0)) and self.retraction1 == True:
                for n in range(20,0,-1):
                    self.position = (n*math.pi)/180
                    #rospy.loginfo(self.position)
                    self.pub7.publish(self.position)
                    self.pub8.publish(self.position)
                    self.pub9.publish(self.position)
                    rospy.sleep(0.01)
                self.retraction2 = True
        else:
            if self.retraction3 == True:
                rospy.sleep(0.05)
                for i1 in range(0,20):
                    self.position = (i1*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub4.publish(self.position)
                    rospy.sleep(0.007)
                for i1 in range(0,12):
                    self.position = (i1*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub1.publish(self.position)
                    rospy.sleep(0.007)
                for j1 in range(20,-2,-1):
                    self.position = (j1*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub4.publish(self.position)
                    rospy.sleep(0.007)
                for i2 in range(0,20):
                    self.position = (i2*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub10.publish(self.position)
                    rospy.sleep(0.007)
                for i2 in range(0,12):
                    self.position = (i2*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub7.publish(self.position)
                    rospy.sleep(0.007)
                for j2 in range(20,-2,-1):
                    self.position = (j2*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub10.publish(self.position)
                    rospy.sleep(0.007)
                for i3 in range(0,20):
                    self.position = (i3*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub5.publish(self.position)
                    rospy.sleep(0.007)
                for i3 in range(0,12):
                    self.position = (i3*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub2.publish(self.position)
                    rospy.sleep(0.007)
                for j3 in range(20,-2,-1):
                    self.position = (j3*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub5.publish(self.position)
                    rospy.sleep(0.007)
                for i4 in range(0,20):
                    self.position = (i4*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub12.publish(self.position)
                    rospy.sleep(0.007)
                for i4 in range(0,12):
                    self.position = (i4*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub9.publish(self.position)
                    rospy.sleep(0.007)
                for j4 in range(20,-2,-1):
                    self.position = (j4*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub12.publish(self.position)
                    rospy.sleep(0.007)
                for i5 in range(0,20):
                    self.position = (i5*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub6.publish(self.position)
                    rospy.sleep(0.007)
                for i5 in range(0,12):
                    self.position = (i5*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub3.publish(self.position)
                    rospy.sleep(0.007)
                for j5 in range(20,-2,-1):
                    self.position = (j5*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub6.publish(self.position)
                    rospy.sleep(0.007)
                for i6 in range(0,20):
                    self.position = (i6*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub11.publish(self.position)
                    rospy.sleep(0.007)
                for i6 in range(0,12):
                    self.position = (i6*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub8.publish(self.position)
                    rospy.sleep(0.007)
                for j6 in range(20,-2,-1):
                    self.position = (j6*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub11.publish(self.position)
                    rospy.sleep(0.007)
                self.retraction3 = False
            if (self.c1 != 0 and self.c2 != 0 and self.c3 != 0) or (self.c1 != 0 and self.c3 != 0 and self.c4 != 0) or (self.c1 != 0 and self.c4 != 0 and self.c5 != 0) or (self.c1 != 0 and self.c5 != 0 and self.c6 != 0) or (self.c2 != 0 and self.c3 != 0 and self.c4 != 0) or (self.c2 != 0 and self.c4 != 0 and self.c5 != 0) or (self.c2 != 0 and self.c5 != 0 and self.c6 != 0) or (self.c3 != 0 and self.c4 != 0 and self.c5 != 0) or (self.c3 != 0 and self.c5 != 0 and self.c6 != 0) or (self.c4 != 0 and self.c5 != 0 and self.c6 != 0) or (self.c1 != 0 and self.c2 != 0 and self.c5 != 0) or (self.c2 != 0 and self.c5 != 0) or (self.c3 != 0 and self.c4 != 0) or (self.c4 != 0 and self.c6 != 0) or (self.c1 != 0 and self.c6 != 0) or (self.c1 != 0 and self.c3 != 0 and self.c5 != 0) or (self.c2 != 0 and self.c4 != 0 and self.c6 != 0):
                for k0 in range(12,0,-1):
                    self.position = (k0*math.pi)/180
                    #rospy.loginfo(position)
                    self.pub1.publish(self.position)
                    self.pub7.publish(self.position)
                    self.pub2.publish(self.position)
                    self.pub9.publish(self.position)
                    self.pub3.publish(self.position)
                    self.pub8.publish(self.position)
                    rospy.sleep(0.007)
                self.retraction3 = True

            
    #def callback0(data):
     #   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.range)
      #  sonar0 = int(data.range)
    #def callback1(data):
     #   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.range)
       # sonar1 = data.range
    #def callback2(data):
     #   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.range)
      #  sonar2 = data.range
    #def callback3(data):
     #   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.range)
      #  sonar3 = data.range
    #def callback4(data):
     #   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.range)
      #  sonar3 = data.range
    #def callback5(data):
     #   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.range)
      #  sonar3 = data.range
    #def callback6(data):
     #   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.range)
      #  sonar3 = data.range
    
    
    



        
        
        

if __name__ == '__main__':
    rospy.init_node('hexa_talker', anonymous=True)
    a= hexa_walking_control()
    rospy.spin()


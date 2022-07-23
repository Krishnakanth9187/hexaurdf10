#!/usr/bin/env python3

import rospy
from hexaurdf10_gazebo.hexaurdf10 import Hexaurdf10


if __name__ == '__main__':
    rospy.init_node('walker_demo')

    rospy.loginfo('Instantiating robot Client')
    robot = Hexaurdf10()
    rospy.sleep(1)

    rospy.loginfo('Walker Demo Starting')
    robot.set_walk_velocity(1, 1, 0)
    rospy.sleep(4)
    robot.set_walk_velocity(0, 0, 0)
    rospy.loginfo('Walker Demo Finished')

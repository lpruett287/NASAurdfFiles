#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
## main logic of the node 
def main():
	## user rospy to create node nasa_control
    rospy.init_node('nasa_control')
    ## create publisher object the publishes to the /simple_model/diff_drive_controller/cmd_vel topic 		whith msg type twist
    pub = rospy.Publisher('/simple_model/diff_drive_controller/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # publishing rate in hz
    move_cmd = Twist() ## create object of msg type twist 
    move_cmd.linear.x = 1.0## assinge liner and anguler value
    move_cmd.angular.z = 10000000.0
    now = rospy.Time.now()## get the current time 
    rate = rospy.Rate(10)
    while rospy.Time.now() < now + rospy.Duration.from_sec(6):
        pub.publish(move_cmd)##publish the command to the topic 
        rate.sleep() 
    rospy.spin()


if __name__ =='__main__':
    main()

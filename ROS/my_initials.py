#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI= 3.14159265
def my_initials():
    rospy.init_node('my_initials', anonymous='True')
    pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel=Twist()

    vel.linear.x=2.0
    vel.angular.z=1.8
    current_angle=0.0
    relative_angle=PI
    t0=rospy.Time.now().to_sec()
    while (current_angle<relative_angle):
        pub.publish(vel)
        t1=rospy.Time.now().to_sec()
        current_angle=1.7*(t1-t0)
    
    vel.linear.x=2.0
    vel.angular.z=-1.8
    current_angle=0.0
    relative_angle=PI
    t0=rospy.Time.now().to_sec()
    while (current_angle<relative_angle):
        pub.publish(vel)
        t1=rospy.Time.now().to_sec()
        current_angle=1.8*(t1-t0)	
    
    vel.angular.z=0
    vel.linear.x=0
    pub.publish(vel)
    rospy.spin()

if __name__ == '__main__':
    try:
        my_initials()
    except rospy.ROSInterruptException:
        pass

    


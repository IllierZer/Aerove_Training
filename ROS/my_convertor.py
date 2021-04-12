#!/usr/bin/env python
import rospy
import math as m
from beginner_tutorials.msg import quaternions
from beginner_tutorials.msg import euler_angles
e=euler_angles()
PI=3.1415926535


def callback(q):
    pub=rospy.Publisher('topic2',euler_angles)
    sinr_cosp= 2* (q.w*q.x + q.y*q.z)
    cosr_cosp=1- 2*(q.x*q.x +q.y*q.y)
    e.roll=m.atan2(sinr_cosp,cosr_cosp)
   
    sinp= 2*(q.w*q.y -q.z*q.x)
    if (abs(sinp)>=1):
        e.pitch=m.copysign(PI/2,sinp)
    else :
        e.pitch=m.asin(sinp)

    siny_cosp =2*(q.w*q.z +q.x*q.y)
    cosy_cosp= 1- 2*(q.y*q.y + q.z*q.z)
    e.yaw=m.atan2(siny_cosp,cosy_cosp) 
    pub.publish(e)
    rospy.loginfo("roll : %s" % e.roll)
    rospy.loginfo("pitch : %s" % e.pitch)
    rospy.loginfo("yaw : %s" % e.yaw)
    
  
                    
def subs():        
    rospy.init_node('my_convertor',anonymous='True')
    sub=rospy.Subscriber('topic1',quaternions, callback)
    rospy.spin()

if __name__ == '__main__':
    try: 
        subs()
    except ROSInterruptException:
        pass
    

    





    
    
    
    
    

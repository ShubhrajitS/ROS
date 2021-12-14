import rospy
from geometry_msgs.msg import Twist
rospy.init_node('myController')

pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

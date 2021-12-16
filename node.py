import rospy
from geometry_msgs.msg import Twist

rospy.init_node('myController')  # Creating a node

pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10) # create a publisher

msg = Twist()

msg.linear.x =1

while not rospy.is_shutdown():
	pub.publish(msg)

print('yes')

print('Hello')

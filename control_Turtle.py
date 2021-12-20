import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

def move_turtle(x_vel,y_vel,ang_vel,t):
	rospy.init_node('turtleMove')
	pub= rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	rate = rospy.Rate(10)

	vel= Twist()


	for i in range(t):
		vel.linear.x = x_vel
		vel.linear.y = y_vel
		vel.linear.z =0

		vel.angular.x=0
		vel.angular.y=0
		vel.angular.z=ang_vel

		pub.publish(vel)
		rate.sleep()


move_turtle(1,0,0,20)
move_turtle(0,0,1.5,1)

sub = rospy.Subscriber('/turtle1/pose',Pose)




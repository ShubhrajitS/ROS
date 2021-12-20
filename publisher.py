import rospy
from std_msgs.msg import String

rospy.init_node('myPublisher')

pub= rospy.Publisher('/exampleTopic', String, queue_size=10)

msg= 'Hello'

while not rospy.is_shutdown():
	pub.publish(msg)


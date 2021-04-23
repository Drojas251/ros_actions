#!/usr/bin/env python

import rospy
import actionlib

from my_robot_msgs.msg import CountUntilAction  # for actions you just need to import the messge ' my_robot_msgs.msg'
from my_robot_msgs.msg import CountUntilGoal
from my_robot_msgs.msg import CountUntilResult

class CountUntilServer:
	
	def __init__(self):
    		#      Initialize the server             Topic name       Data type            callback (cb)          auto start the server = false
    		self._as = actionlib.SimpleActionServer('/count_until', CountUntilAction, execute_cb= self.get_goal, auto_start= False)
		self._as.start() # here we can manually start the server.

		self._counter = 0
		rospy.loginfo("Aerver has started")
		# for a robot arm with moveit, we can initialize movite parametes arm_group = moveitcommander ect here in the constructor

	def get_goal(self,goal):
    		rospy.loginfo("A goal has been recieve")
		rospy.loginfo(goal)

		max_number = goal.max_number
		wait_duration = goal.wait_duration

		self._counter = 0
		rate = rospy.Rate(1.0/wait_duration)

		while self._counter < max_number:
    			self._counter += 1
			rospy.loginfo(self._counter)
			rate.sleep()
		result = CountUntilResult()
		result.count = self._counter
		# how to send the result ?

		self._as.set_succeeded(result)

if __name__ == '__main__':
    	rospy.init_node('count_until_server')

	server = CountUntilServer()
	rospy.spin()
    		

#!/usr/bin/env python

import rospy
import actionlib

from my_robot_msgs.msg import CountUntilAction
from my_robot_msgs.msg import CountUntilGoal

class CountUntilClient:

    def __init__(self):
        self._ac = actionlib.SimpleActionClient('/count_until',CountUntilAction) # initialize client ' same topic '
        self._ac.wait_for_server() # wait for server to be up ** important 
        rospy.loginfo("action server is up")

    def send_goal_and_get_results(self):
        goal = CountUntilGoal(max_number = 12, wait_duration = 0.5)
        # how to send the goal?
        # use a call back to trigger the goal. Needed to make action asynchronous
        self._ac.send_goal(goal, done_cb= self.done_callback, feedback_cb = self.feedback_callback)
        rospy.loginfo("goal has been sent")
        # now we need to get result
        #self._ac.wait_for_result()
        #self._ac.get_result()
        #rospy.loginfo(self._ac.get_result())

	rospy.sleep(2)
	self._ac.cancel_goal() # method to request the serve to cancel a goal

    def done_callback(self,status,result):
        rospy.loginfo("Status is: " + str(status))
        rospy.loginfo("Result is: " + str(result))

    def feedback_callback(self,feedback):
	rospy.loginfo(feedback)

if __name__ == '__main__':
    rospy.init_node('count_until_client')
    client = CountUntilClient()
    client.send_goal_and_get_results()
    rospy.spin()

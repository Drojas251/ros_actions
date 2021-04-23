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
        goal = CountUntilGoal(max_number = 10, wait_duration = 0.5)
        # how to send the goal?
        self._ac.send_goal(goal)
        rospy.loginfo("goal has been sent")
        success = self._ac.wait_for_result(rospy.Duration(3.0)) #  returns a boolean if results take longer than 3s
        if not success:
            rospy.loginfo("TIMEOUT")
        # now we need to get result
        self._ac.wait_for_result()
        self._ac.get_result()
        rospy.loginfo(self._ac.get_result())

if __name__ == '__main__':
    rospy.init_node('count_until_client')
    client = CountUntilClient()
    client.send_goal_and_get_results()

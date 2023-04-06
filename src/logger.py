#!/usr/bin/env python3

import rospy
import csv
from ar_track_alvar_msgs.msg import AlvarMarkers

#declaring variables, honestly don't know if this is bad python practice
ID_list = []
current_marker = 999 #placeholder variable to prevent logging the same ID more than once

def callback_ar_pose(msg):
    for marker in msg.markers:
        # These two just print the ID and Pose to the cmd line
        #rospy.loginfo(marker.id)
        #rospy.loginfo(marker.pose.pose)
        if marker.id != current_marker: # Check to prevent multi-logging
            current_marker = marker.id
            ID_list.append(current_marker)
            rospy.loginfo(current_marker)
            rospy.loginfo(ID_list)

            


if __name__ == "__main__":
        rospy.init_node("ar_logger")

        ar_subscriber = rospy.Subscriber( 
            "ar_pose_marker", AlvarMarkers, callback_ar_pose  
        )
        rospy.spin()


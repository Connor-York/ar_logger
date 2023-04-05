#!/usr/bin/env python3

import rospy

from ar_track_alvar_msgs.msg import AlvarMarkers

def callback_ar_pose(msg):
    for marker in msg.markers:
        rospy.loginfo(marker.id)
        rospy.loginfo(marker.pose.pose)



if __name__ == "__main__":
        rospy.init_node("ar_logger")

        ar_subscriber = rospy.Subscriber( 
            "ar_pose_marker", AlvarMarkers, callback_ar_pose  
        )
        rospy.spin()


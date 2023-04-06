#!/usr/bin/env python3

import rospy
import csv
from ar_track_alvar_msgs.msg import AlvarMarkers
import rospkg
rp = rospkg.RosPack()
package_path = rp.get_path('ar_logger')

#declaring variables, honestly don't know if this is bad python practice
ID_list = []
current_marker = 999 #placeholder variable to prevent logging the same ID more than once
CSV_path = (package_path + "/logs/IDlog.csv")

def dupe_check(iterable,check):
    for x in iterable:
        if x == check:
            return True

def callback_ar_pose(msg):
    for marker in msg.markers:
        global ID_list
        global current_marker
        # These two just print the ID and Pose to the cmd line
        #rospy.loginfo(marker.id)
        #rospy.loginfo(marker.pose.pose)
        if marker.id != current_marker: # Check to prevent multi-logging
            current_marker = marker.id
            if dupe_check(ID_list,current_marker) == True:
                continue
            else:
                ID_list.append(current_marker)
            rospy.loginfo(current_marker)
            rospy.loginfo(ID_list)

def save_to_csv():
    
    with open(CSV_path, 'w') as f:

        writer = csv.writer(f)

        writer.writerow(ID_list)


if __name__ == "__main__":
        rospy.init_node("ar_logger")

        ar_subscriber = rospy.Subscriber( 
            "ar_pose_marker", AlvarMarkers, callback_ar_pose  
        )
        rospy.spin()
        rospy.on_shutdown(save_to_csv)


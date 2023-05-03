#!/usr/bin/env python3

import rospy
import csv
from ar_track_alvar_msgs.msg import AlvarMarkers
import rospkg
import datetime 


#declaring global
ID_list = []
Time_list = []
current_marker = 999 #placeholder variable to prevent logging the same ID more than once

#getting date for saving
current_date = datetime.date.today()
formatted_date = current_date.strftime("%Y-%m-%d")

#gets csv file path for saving
rp = rospkg.RosPack()
package_path = rp.get_path('ar_logger')
CSV_path = (package_path + "/logs/IDlog" + formatted_date + ".csv")





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
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%H:%M:%S")
            if dupe_check(ID_list,current_marker) == True:
                continue
            else:
                Time_list.append(formatted_time)
                ID_list.append(current_marker)
            rospy.loginfo(current_marker)
            rospy.loginfo(ID_list)

def save_to_csv(): #called on shutdown, saves csv, overwrites file
    
    with open(CSV_path, 'w') as f:

        writer = csv.writer(f)

        writer.writerow(ID_list)
        writer.writerow(Time_list)


if __name__ == "__main__":
        rospy.init_node("ar_logger")

        ar_subscriber = rospy.Subscriber( 
            "ar_pose_marker", AlvarMarkers, callback_ar_pose  
        )

        rospy.spin()
        rospy.on_shutdown(save_to_csv) #call on shutdown



#!/usr/bin/env python3

import rospy
import csv
from ar_track_alvar_msgs.msg import AlvarMarkers
import rospkg
import datetime 
import time

#declaring global
ID_list = []
Time_list = []
#current_marker = 999 #placeholder variable to prevent logging the same ID more than once
buffer = []

#getting date for saving
current_date = datetime.date.today()
formatted_date = current_date.strftime("%Y-%m-%d")
current_time_save = datetime.datetime.now()
current_time_save = current_time_save.strftime("%H:%M:%S")

start_time = time.time()

#gets csv file path for saving
rp = rospkg.RosPack()
package_path = rp.get_path('ar_logger')
CSV_path = (package_path + "/logs/IDlog_" + formatted_date + "_" + current_time_save + ".csv")





def dupe_check(iterable,check):
    for x in iterable:
        if x == check:
            return True

def buffer_check(buffer,check):
  buffer.append(check)
  if len(buffer) == 11:
    buffer.pop(0)
  tick = 0
  for x in buffer: 
    if x == check:
      tick += 1
      if tick == 3:
        return True

def callback_ar_pose(msg):
    for marker in msg.markers:

        # These two just print the ID and Pose to the cmd line
        #rospy.loginfo(marker.id)
        #rospy.loginfo(marker.pose.pose)
        #print(marker.id)
#        print(buffer)
#        print(ID_list)
    
        #filter out fake IDs (>17), any IDs already in the list, and only accept those that have been seen thrice
        if buffer_check(buffer,marker.id):
            if marker.id < 18 and dupe_check(ID_list, marker.id) == None:
                current_time = time.time()
                elapsed_time = current_time - start_time
                Time_list.append(elapsed_time)
                ID_list.append(marker.id)
            


        ## OLD CODE \/

        # if marker.id != current_marker: # Check to prevent multi-logging
        #     current_time = time.time()
        #     elapsed_time = current_time - start_time
        #     current_marker = marker.id 
        #     if dupe_check(ID_list,current_marker) == True:
        #         continue
        #     else:
        #         Time_list.append(elapsed_time)
        #         ID_list.append(current_marker)
        #     rospy.loginfo(current_marker)
        #     rospy.loginfo(elapsed_time)
        #     rospy.loginfo(ID_list)

def save_to_csv(): #called on shutdown, saves csv
    
    #with open(CSV_path, 'w') as f:
    #
    #    writer = csv.writer(f)
    #
    #   writer.writerow(ID_list)
    #    writer.writerow(Time_list)

    with open(CSV_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Timestamp"])
        for i in range(len(ID_list)):
            writer.writerow([ID_list[i], Time_list[i]])
        end_time = time.time()
        elapsed_time = end_time - start_time
        writer.writerow([999, elapsed_time])


if __name__ == "__main__":
        rospy.init_node("ar_logger")

        ar_subscriber = rospy.Subscriber( 
            "ar_pose_marker", AlvarMarkers, callback_ar_pose  
        )

        rospy.spin()
        rospy.on_shutdown(save_to_csv) #call on shutdown



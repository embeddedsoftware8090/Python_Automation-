# from infi.devicemanager import DeviceManager
# dm = DeviceManager()
# dm.root.rescan()
# devices = dm.all_devices
# for device in devices:
#     print(device)

# #---------------------------------
#get executable file and get process id as well
# import wmi
# # Initializing the wmi constructor
# f = wmi.WMI()
# # Printing the header for the later columns
# print("pid      Process name")
# # Iterating through all the running processes
# for process in f.Win32_Process():
#     # Displaying the P_ID and P_Name of the process
#     print(f"{process.ProcessId:<10} {process.Name}")



# import win32api
# import win32con
# import pywintypes
# width=int(input('Enter the Width: '))
# height=int(input('Enter the Height: '))
#
# devmode = pywintypes.DEVMODEType()
#
# devmode.PelsWidth = width
# devmode.PelsHeight = height
#
# devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
#
# win32api.ChangeDisplaySettings(devmode, 0)
#
# print(abs(-34))
#
# print( all([True, True, True]))
# # print(all((0, True, False)))
# print(all({1, 1, 1}))
#
# print(any((0, True, False)))
#
# print(ascii('A'))
# print(ascii('26'))
#
#
# # Create a loop over 5 integers
# for i in range(5):
#     # Stream i to stdout
#     print(i)
#     # Create breakpoint at # 3
#     if i == 3:
#         breakpoint()

# import calendar
# import datetime
#
# p =datetime.datetime(2022,10,22)
# print(p)

# import keyword
# print(keyword.kwlist)

#---------------------------------------------------------
# a ,b,c,d,e =[int(x) for x in input("Enter the Numbers:\n").split()]
# pro = a+b+c+d+e
# print(pro)

#------------------------------------------------------
# l = eval(input("Enter the numbers:\n"))
# print (type(l))
# print(l)

# from sys import argv
# print("The Number of Command Line Arguments:", len(argv))
# print("The List of Command Line Arguments:", argv)
# print("Command Line Arguments one by one:")
# for x in argv:
#     print(x)




# 1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
# 2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
# 3) isdigit(): Returns True if all characters are digits only( 0 to 9)
# 4) islower(): Returns True if all characters are lower case alphabet symbols
# 5) isupper(): Returns True if all characters are upper case aplhabet symbols
# 6) istitle(): Returns True if string is in title case
# 7) isspace(): Returns True if string contains only spaces

# str1= "balkumar"
# print(''.join(reversed(str1)))
#
# i =len(str1)-1
# print(i)
# target =""
# while i>=0:
#     target = target+str1[i]
#     i -=1
# print(target)


# s = input("Enter the strings:\n")
# l = []
# for x in s:
#     if x not in l:
#         l.append(x)
#         res ="".join(l)
# print(res)
#
#

# num = 0x11111

# import bits
# from ctypes import *
# mem = (c_char * 128).from_address(0xf1390)
# print (bits.dumpmem(mem))


# import acpi
# print(acpi.get_table_list())


# import platform
# import subprocess
#
# if '32bit' in platform.architecture():
#     process = '%systemroot%\Sysnative\pnputil.exe -e'
# else:
#     process = 'pnputil.exe -e'
#
# p = subprocess.Popen(process, shell=True,
#         stdout=subprocess.PIPE, universal_newlines=True)
#--------------------------------------------------
# import this
# import antigravity


# import psutil
# print("physical core",psutil.cpu_count(logical=False))
# print("logical core",psutil.cpu_count(logical=True))
# print("socket",psutil)
# print("currrent cpu utilization",psutil.cpu_percent(interval=1) )

# How to Perform Motion Detection Using Python

# Importing the Pandas libraries
import pandas as panda

# Importing the OpenCV libraries
import cv2

# Importing the time module
import time

# Importing the datetime function of the datetime module
from datetime import datetime

# Assigning our initial state in the form of variable initialState as None for initial frames
initialState = None

# List of all the tracks when there is any detected of motion in the frames
motionTrackList = [None, None]

# A new list 'time' for storing the time when movement detected
motionTime = []

# Initialising DataFrame variable 'dataFrame' using pandas libraries panda with Initial and Final column
dataFrame = panda.DataFrame(columns=["Initial", "Final"])

# starting the webCam to capture the video using cv2 module
video = cv2.VideoCapture(0)

# using infinite loop to capture the frames from the video
while True:

    # Reading each image or frame from the video using read function

    check, cur_frame = video.read()

    # Defining 'motion' variable equal to zero as initial frame

    var_motion = 0

    # From colour images creating a gray frame

    gray_image = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)

    # To find the changes creating a GaussianBlur from the gray scale image

    gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)

    # For the first iteration checking the condition

    # we will assign grayFrame to initalState if is none

    if initialState is None:
        initialState = gray_frame

        continue

        # Calculation of difference between static or initial and gray frame we created

    differ_frame = cv2.absdiff(initialState, gray_frame)

    # the change between static or initial background and current gray frame are highlighted

    thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # For the moving object in the frame finding the coutours

    cont, _ = cv2.findContours(thresh_frame.copy(),

                               cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cur in cont:

        if cv2.contourArea(cur) < 10000:
            continue

        var_motion = 1

        (cur_x, cur_y, cur_w, cur_h) = cv2.boundingRect(cur)

        # To create a rectangle of green color around the moving object

        cv2.rectangle(cur_frame, (cur_x, cur_y), (cur_x + cur_w, cur_y + cur_h), (0, 255, 0), 3)

        # from the frame adding the motion status

    motionTrackList.append(var_motion)

    motionTrackList = motionTrackList[-2:]

    # Adding the Start time of the motion

    if motionTrackList[-1] == 1 and motionTrackList[-2] == 0:
        motionTime.append(datetime.now())

        # Adding the End time of the motion

    if motionTrackList[-1] == 0 and motionTrackList[-2] == 1:
        motionTime.append(datetime.now())

        # In the gray scale displaying the captured image

    cv2.imshow("The image captured in the Gray Frame is shown below: ", gray_frame)

    # To display the difference between inital static frame and the current frame

    cv2.imshow("Difference between the  inital static frame and the current frame: ", differ_frame)

    # To display on the frame screen the black and white images from the video

    cv2.imshow("Threshold Frame created from the PC or Laptop Webcam is: ", thresh_frame)

    # Through the colour frame displaying the contour of the object

    cv2.imshow("From the PC or Laptop webcam, this is one example of the Colour Frame:", cur_frame)

    # Creating a key to wait

    wait_key = cv2.waitKey(1)

    # With the help of the 'm' key ending the whole process of our system

    if wait_key == ord('m'):

        # adding the motion variable value to motiontime list when something is moving on the screen

        if var_motion == 1:
            motionTime.append(datetime.now())

        break

    # At last we are adding the time of motion or var_motion inside the data frame
for a in range(0, len(motionTime), 2):
    dataFrame = dataFrame.append({"Initial": time[a], "Final": motionTime[a + 1]}, ignore_index=True)

# To record all the movements, creating a CSV file
dataFrame.to_csv("EachMovement.csv")

# Releasing the video
video.release()

# Now, Closing or destroying all the open windows with the help of openCV
cv2.destroyAllWindows()
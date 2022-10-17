import os
import pyautogui as pg
import cv2
import cv2_tools
import aoirint_cv2videotools
import time
from time import sleep
from datetime import datetime

os.startfile(r"C:/Users/Balkumar/Downloads/cpu-z_2.02-en/cpuz_x64.exe")
sleep(5)

pg.leftClick(613,20)
time.sleep(2)
# try:
#     # open MS Teams application
#     os.startfile(r"C:/Users/Balkumar/Downloads/cpu-z_2.02-en/cpuz_x64.exe")
#     sleep(5)
#     pyautogui.click(612,202)
#     # settings
#     img=cv2.imread('m.png')
#     #img =aoirint_cv2videotools.FileLoader(r"C:\Desktop\memory.PNG")
#     settings = pyautogui.locateCenterOnScreen("img")
#     pyautogui.moveTo(settings)
#     pyautogui.click()
#     time.sleep(2)
# except Exception:
#     print("")

#----------------------------------------------------------------------------
# # #------------------- oppenning any application
# import os
# import pywinauto,time
# from pywinauto.application import Application
# from pywinauto.keyboard import send_keys
# app =os.startfile("C:/Users/Balkumar/Downloads/cpu-z_2.02-en/cpuz_x64.exe")
# #os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/System Tools/Task Manager.lnk")
# time.sleep(5)

#--------------------------------------------------------------------------------

#get all exe file fow windows
# import subprocess
# cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# for line in proc.stdout:
#     print(line)
#


# import subprocess
# cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# for line in proc.stdout:
#     if line.rstrip():
#         # only print lines that are not empty
#         # decode() is necessary to get rid of the binary string (b')
#         # rstrip() to remove `\r\n`
#         print(line.decode().rstrip())
# -----------------------------------------------------------------------------------
# import subprocess
# cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description,Id,Path'
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# for line in proc.stdout:
#     if not line.decode()[0].isspace():
#         print(line.decode().rstrip())

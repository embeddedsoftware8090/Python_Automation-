#Method1
# import os
# #os.system(taskkill /f notepad.exe)
# #taskkill /f /fi "USERNAME eq NT AUTHORITY\SYSTEM" /im notepad.exe
# os.system("taskkill /f /im  notepad.exe")
# os.system("taskkill /f /im  chrome.exe") #chrome process

##Method2
import os

def terminate(ProcessName):
    os.system('taskkill /IM "' + ProcessName + '" /F')
terminate('notepad.exe')
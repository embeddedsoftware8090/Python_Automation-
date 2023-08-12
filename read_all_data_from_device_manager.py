import subprocess
#x =open("data.txt","w+ ")
subprocess.run(["powershell.exe",
                    r'Get-WmiObject Win32_PnPSignedDriver | select devicename, driverversion'],)
# print(y)
# print(subprocess.run(["powershell.exe",
#                     r'Get-WmiObject Win32_PnPSignedDriver | select devicename, driverversion'],),file=x)



# #speaker properties
# import subprocess
# subprocess.run(["powershell .exe",
#                 '-ExecutionPolicy',
#                 'Unrestricted',
#                 r'Get-CimInstance win32_sounddevice | fl *'],)



# brightness level
# import screen_brightness_control
# print(screen_brightness_control.get_brightness())



# #monitor resolution
# import pyautogui
# resolution = pyautogui.size()
# print("Monitor Resolution is: ",resolution)

# import os
# os.startfile("devmgmt.msc")
#
# import WMI
from infi.devicemanager import DeviceManager

dm = DeviceManager()
dm.root.rescan()
disks = dm.disk_drives
names = [disk.friendly_name for disk in disks]
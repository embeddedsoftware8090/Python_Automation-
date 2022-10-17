import subprocess
p = subprocess.run(["powershell.exe",
                    r'Get-WmiObject Win32_PnPSignedDriver | select devicename, driverversion'],)

# #speaker properties
# import subprocess
# subprocess.run(["powershell .exe",
#                     '-ExecutionPolicy',
#                     'Unrestricted',
#                     r'Get-CimInstance win32_sounddevice | fl *'],
#                    )
#brightness level
import screen_brightness_control
print(screen_brightness_control.get_brightness())

# #monitor resolution
# import pyautogui
# resolution = pyautogui.size()
# print("Monitor Resolution is: ",resolution)

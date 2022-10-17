import pyautogui
import os
import pyautogui as pg
import cv2
import cv2_tools
import aoirint_cv2videotools
import time
from time import sleep
import pywinauto
from pywinauto import mouse
from pywinauto import keyboard
from datetime import datetime
# os.startfile(r"C:/Users/Balkumar/Downloads/cpu-z_2.02-en/cpuz_x64.exe")
# sleep(10)
res =pyautogui.locateAllOnScreen("edit.png")
print(res)
#print(pyautogui.locateAllOnScreen(res))
edit_but=pyautogui.center(res)
pyautogui.moveTo(res)
time.sleep(3)
pywinauto.mouse.click()
#pyautogui.hotkey('enter')
#time.sleep(5)
#pywinauto.mouse.double_click(button= 'left',coords=(901,184))
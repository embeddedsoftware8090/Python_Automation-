# reading a data from file on notepad or console window
from pywinauto import application
import time
app=application.Application()
app.start("Notepad.exe")#open file
time.sleep(2)
app.Notepad.menu_select("File->open") #click open option
app.Open.Edit.set_edit_text("Bal.txt") #text file save as Bal.txt
time.sleep(2)
app.Open.Open.click(double=True) #double click
print(app.Notepad.Edit.window_text())#printing data on consol window



#writing a data in notepad and save as test.txt
# from pywinauto import application
# import time
# app=application.Application()
# app.start("Notepad.exe")#open file
# time.sleep(4)
# app.Edit.set_edit_text("Hi My Name Is Balkumar")









# n1,n2 =0,1
# print(n1,n2)
# for x in range(10):
#     n3 = n1+n2
#     n1=n2
#     n2=n3
#     print(n3)

#------------------------------
# numbers  = 153
# temp =numbers
# sum =0
# while numbers>=1:
#     rem = numbers %10
#     sum = sum+rem * rem * rem
#     numbers = numbers//10
# if temp == sum :
#     print("Armstrong Number")
# else:
#     print("Bye Deepika")













#------------------------------------------------------------------------

# import os
# import pywinauto,time
# from pywinauto.application import Application
# from pywinauto.keyboard import send_keys
# app = Application().start("Notepad.exe" )
# time.sleep(1)
# #app.UntitleNotepad.menu_select("Help->About Notepad") #view about notepad
# app.UntitleNotepad.menu_select("file->Save as")
# app.FileName.send_keys("test.txt")
# dlg =app.window(title_re="note")
#-----------------------------------------------------------------------------
###########  Notepad
# import pywinauto
# import time
# from pywinauto.application import Application
# from subprocess import Popen
# from pywinauto import Desktop
# app = Application().start('notepad.exe')#oppenning Note Pad with untitle
# #dlg = app.window(title_re=".*Notepad.*")
# app.UntitledNotepad.menu_select("Edit -> Replace")
# app.Replace.print_control_identifiers()

#------------------------------------------------------------------

#from pywinauto import application
# # import subprocess
# # subprocess.call('ipconfig',shell=True)
#----------------------------------------------------------------------
# #access firewall
# import subprocess
# p=subprocess.run("netsh advfirewall show all profiles")


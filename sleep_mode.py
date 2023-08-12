import  os
#os.system("shutdown /u")
#os.system("shutdown /h")
#os.system("shutdown /r")

#----------------------------------------------
# import os
# user=input("Enter to shutdown, restart,sleep or hibernate:\n")
# if user=="shutdown":
#     os.system("shutdown /u /t 1") #shutdown the system
# elif user=='restart':
#     os.system("shutdown /r /t 1")#restart the system
# elif user=="sleep":
#     os.system("shutdown /p /t 1")#sleep the system
# elif user == "hibernate":
#     os.system("shutdown /h /t 1")#hibernate the system
# else:
#     print("bye")
#


# import os
# try:
#
# except:
#     os.system('cmd/k "pwrtest /sleep /c:4 /s:all "')
# print("Not able to keep system in mentioned state")

# import os
# import subprocess
# import pywin32_system32
# import win32api
#
# #subprocess.call('runas','Administrator','cmd.exe')
# import os
# import sys
# import win32com.shell.shell as shell
#
#
# ASADMIN = 'asadmin'
# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#     sys.exit(0)
# subprocess.call('cmd /k   "pwrtest /sleep"')

# import subprocess
# subprocess.call('time',shell=True)
#

import platform
x= open("data.txt","a")
print('OS Name :',platform.system())
print('Host Name :',platform.node())
print('Number :',platform.release())
print('version :',platform.version())
print('HW identifier :',platform.machine())
print('Processor Name :',platform.processor())


print('OS Name :',platform.system(),file=x)
print('Host Name :',platform.node(),file=x)
print('Number :',platform.release(),file=x)
print('version :',platform.version(),file=x)
print('HW identifier :',platform.machine(),file=x)
print('Processor Name :',platform.processor(),file=x)



#system information
# import subprocess
# subprocess.call('Systeminfo')

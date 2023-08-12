import psutil
x=open("data.txt",'a')
print(psutil.cpu_freq())#freqeuncy of CPU
print(psutil.boot_time()) #booting time
print(psutil.pids()) #getting process id
print(psutil.Process())
print(psutil.net_if_addrs())
print(psutil.cpu_stats())

print(psutil.cpu_freq(),file=x)#freqeuncy of CPU
print(psutil.boot_time(),file=x) #booting time
print(psutil.pids(),file=x) #getting process id
print(psutil.Process(),file=x)
print(psutil.net_if_addrs(),file=x)
print(psutil.cpu_stats(),file=x)

#import subprocess
#subprocess.call('start',shell=True)#start the command prompt

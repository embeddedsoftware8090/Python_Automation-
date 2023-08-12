x=open("data.txt",'a')
# from infi.devicemanager import DeviceManager
# dm = DeviceManager()
# dm.root.rescan()
# devices = dm.all_devices
import subprocess
devices= str(subprocess.call("netsh wlan show networks MODE=BSSID",shell=True))

for device in devices:
    print(device)
    print(devices,file=x)



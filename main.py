import platform
import subprocess

if '32bit' in platform.architecture():
    process = '%systemroot%\Sysnative\pnputil.exe -e'
else:
    process = 'pnputil.exe -e'

p = subprocess.Popen(process, shell=True,
        stdout=subprocess.PIPE, universal_newlines=True)
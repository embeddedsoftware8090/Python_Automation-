#mouse info
import subprocess
p = subprocess.run(["powershell.exe",
                    '-ExecutionPolicy',
                    'Unrestricted',
                    r'Get-WmiObject -Class Win32_PointingDevice'],
                   )

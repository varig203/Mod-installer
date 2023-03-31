import platform, os, windowsBackend, linuxBackend

sDownloads = True
sUsrDir = os.path.expanduser('~')

# Detecting operating system
if platform.system() == "Linux":
    print("Linux has been detected")
    linuxBackend.fnForgeInstall()
elif platform.system() == "Windows":
    print("Windows has been detected")
    windowsBackend.test()
else:
    print("Could not find your system version or your system is not supported")


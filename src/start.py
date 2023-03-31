import platform, windowsBackend, linuxBackend

# Detecting operating system
if platform.system == "Linux":
    linuxBackend.test()
elif platform.system == "Windows":
    windowsBackend.test()
else:
    print("Could not find your system version")

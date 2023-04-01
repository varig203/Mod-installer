import platform, os, windowsBackend, linuxBackend

sUsrDir = os.path.expanduser('~')

# Mapping operating systems to functions
os_functions = {
    'Linux': linuxBackend.fnForgeInstall,
    'Windows': windowsBackend.fnForgeInstall
}

# Detecting operating system and running corresponding function
os_name = platform.system()
if os_name in os_functions:
    print(f"{os_name} has been detected")
    os_functions[os_name]()
else:
    print("Could not find your system version or your system is not supported")

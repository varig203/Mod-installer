import os

def fnChangeDir():
    sUsrDir = os.path.expanduser('~')
    os.chdir(sUsrDir + str('/.minecraft'))


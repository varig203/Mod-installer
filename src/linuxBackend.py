import os, requests

sDownloads = True
sUsrDir = os.path.expanduser('~')

# Basically changes directory based on sDownloads
def fnChangeDir():
    if sDownloads == False:
        os.chdir(sUsrDir + str('/.minecraft'))
    elif sDownloads == True:
        os.chdir(sUsrDir + str('/Downloads'))
    
    
def fnForgeInstall():
    # Grabs the forge installer and runs it
    sDownloads = True
    fnChangeDir()
    print('Download directory ' + (os.getcwd()))
    
    url = 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.2-43.2.8/forge-1.19.2-43.2.8-installer.jar'
    r = requests.get(url, allow_redirects = True)
    open('forge-installer.jar', 'wb').write(r.content)
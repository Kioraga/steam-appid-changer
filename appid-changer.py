import os
import time
import subprocess
from configparser import ConfigParser
from utils import *

print("Steam AppID Changer v1.0.0 by Kioraga\n")

config = ConfigParser()

if not os.path.isfile('config.ini'):
    print("config.ini file not found")
    input("Press Enter to exit...")

config.read('config.ini')

path = config.get('Game Target', 'path')
name = config.get('Game Target', 'name')
process = config.get('Game Target', 'process')
appid = config.get('Game Target', 'appid')
patch_appid = config.get('Patch', 'patch_appid')

print("Game path: " + path)
print("Game name: " + name)
print("Game process: " + process)
print("Game appid: " + appid)
print("Patch appid: " + patch_appid + "\n")

if not checkIfProcessRunning(process):
    print(name + " is not running")

    f = open(path + '/steam_appid.txt', 'w')
    f.write(patch_appid)
    f.close()
    print("Steam appid changed to " + patch_appid)

    print("Launching " + name + "...")
    full_path = os.path.join(path, process + '.exe')
    process = subprocess.Popen([full_path], cwd=path, shell=True)

    print(name + " is running")
    process.wait()

    print(name + " is closed")
    print("Restoring Steam appid...")
    f = open(path + '/steam_appid.txt', 'w')
    f.write(appid)
    f.close()
    print("Steam appid restored to " + appid)
    time.sleep(3)
else:
    print(name + " is already running")
    input("Press Enter to exit...")
import os
import sys
import time
import subprocess
import shutil


def setWallpaper(path):
    print("Setting wallpaper to "+path)

    if os.path.exists(path):
        # Modify this line for your own needs.
        command = "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitoreDP-1/workspace0/last-image -s "+path
        subprocess.Popen(command.split(" "))
    else:
        print("ERROR: file not found")

path = sys.argv[1]
wait_time = float(sys.argv[2])

sequence_files = next(os.walk(path), (None, None, []))[2]
print(path)
print(sequence_files)
while True:
    time.sleep(wait_time)
    for i in range(len(sequence_files)):
       # if i.lower().endswith(".png") or i.lower().endswith(".jpg") or i.lower().endswith(".jpeg") or i.lower().endswith(".bmp") or i.lower().endswith(".gif"):
            #setWallpaper(path+"/"+i)
        setWallpaper(path+"/"+"frame-"+str(i)+".bmp")
        time.sleep(wait_time)
        #else:
         #   print("Ignoring "+i+": file is not an image")

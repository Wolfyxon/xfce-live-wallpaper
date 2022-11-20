import os
import sys
import time
import subprocess
import shutil


def setWallpaper(path):
    print("Setting wallpaper to "+path)

    if os.path.exists(path):
        commands = [
            #XFCE
            "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorDP-0/workspace0/last-image -s "+path,
            "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitoreDP-1/workspace0/last-image -s "+path,
            "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/last-image -s "+path,
            "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/last-single-image -s "+path,
            "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s "+path

            #TODO: Add support for GNOME and KDE
        ]
        for i in commands: subprocess.Popen(i.split(" "))
    else:
        print("ERROR: file not found")

path = sys.argv[1]
wait_time = float(sys.argv[2])

print("Listing frames in "+path)
sequence_files = next(os.walk(path), (None, None, []))[2]
print("Running image sequence from: "+path)
print("Frames: \n"+str(sequence_files)+"\nTotal: "+str(len(sequence_files)))
print("Animating")
while True:
    time.sleep(wait_time)
    for i in range(len(sequence_files)):
        setWallpaper(path+"/"+"frame-"+str(i)+".png")
        time.sleep(wait_time)

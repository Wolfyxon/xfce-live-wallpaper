import os
import shutil
import sys
import time
from PIL import Image

formatting = {
    "HEADER": '\033[95m',
    "OKBLUE": '\033[94m',
    "OKCYAN": '\033[96m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m'
}

def welcomePrint():
    print("")
    print(formatting["BOLD"]+"Live wallpaper script for Linux XFCE")
    print(formatting["FAIL"]+"by Wolfyxon")
    print(formatting["ENDC"]+"usage: main.py <type (gif/video/sequence)> <path/to/file (directory if sequence)> <wait time (optional, default is 0.05s)>")
    print(formatting["WARNING"]+"IMPORTANT NOTE: path must be global, Example: /home/you/Videos/video.mp4 NOT: ./video.mp4. Make sure you have imagemagik installed")
    print(formatting["ENDC"])


if len(sys.argv) > 1:
    types = ["-video", "-gif", "-sequence"]
    type = sys.argv[1]
    path = None
    wait_time = 0.05
    if(len(sys.argv)>2): path = sys.argv[2]
    else: print(formatting["FAIL"]+"No path specified")
    if(len(sys.argv)>3): wait_time = float(sys.argv[3])

    if type in types:
        if(os.path.exists(path)):
            print("Clearing cache and preparing for conversion please wait...")
            shutil.rmtree('./cache', ignore_errors=True)
            os.mkdir("./cache")
            print("Done")
            if type == "-sequence":
                print("Animating image sequence in "+path)
                os.system("python wallpaper.py "+path+" "+str(wait_time))
            if type == "-gif":
                print("Converting GIF to image sequence, please wait...")
                os.system("convert "+path+" -coalesce cache/frame.bmp")
                os.system("python "+os.path.abspath("./wallpaper.py")+" "+os.path.abspath("./cache")+" "+str(wait_time))
            if type == "-video":
                print("Converting video file to image sequence, please wait...")
                os.system("ffmpeg -i "+path+" -vf fps=30 cache/frame-%d.bmp")
                os.system("python " + os.path.abspath("./wallpaper.py") + " " + os.path.abspath("./cache") + " " + str(wait_time))
        else:
            print(formatting["FAIL"] + "This path does not exist")

    else: print(formatting["FAIL"]+"Unknown type")

else:
    print(formatting["FAIL"]+"No arguments specified")
    welcomePrint()
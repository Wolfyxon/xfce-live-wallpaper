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
    print(formatting["ENDC"]+"usage: main.py <type> <path/to/file (directory if sequence)> <wait time (optional, default is 0.05s)>")
    print("""Available types:
    - gif : Converts GIF file into frames then runs animation. (Best quality)
    - video : Converts video file into frames then runs animation. (Worst quality)
    - cache : Uses last cached animation
    """)
    print(formatting["WARNING"]+"IMPORTANT NOTE: path must be global, Example: /home/you/Videos/video.mp4 NOT: ./video.mp4. Make sure you have imagemagik installed")
    print(formatting["ENDC"])

def clearCache():
    print("Clearing cache...")
    shutil.rmtree('./cache', ignore_errors=True)
    os.mkdir("./cache")

def runFromCache():
    os.system("python " + os.path.abspath("./wallpaper.py") + " " + os.path.abspath("./cache") + " " + str(wait_time))

wait_time = 0.05
path = None
type = None

def main():
    global type
    global wait_time
    global path

    if len(sys.argv) > 1:
        types = ["-video", "-gif", "-sequence","-cache"]
        type = sys.argv[1]

        if(len(sys.argv)>3): wait_time = float(sys.argv[3])

        #Doesn't require path
        if type in types:
            if type == "-cache":
                print("Using last cached animation")
                runFromCache()
                return

        #Require path
        if(len(sys.argv)>2): path = sys.argv[2]
        else: print(formatting["FAIL"]+"No path specified")
        if(os.path.exists(path)):
            print("Killing other wallpaper instances...")
            os.system("nohup " + os.path.abspath("./kill.sh") + " &")
            print("Done")
            if type == "-sequence":
                print("Animating image sequence in "+path)
                os.system("python wallpaper.py "+path+" "+str(wait_time))
            if type == "-gif":
                clearCache()
                print("Converting GIF to image sequence, please wait...")
                os.system("convert "+path+" -coalesce cache/frame.png")
                runFromCache()
            if type == "-video":
                clearCache()
                print("Converting video file to image sequence, please wait...")
                os.system("ffmpeg -i "+path+" -vf fps=30 -vf scale=1280:720 cache/frame-%d.png")
                runFromCache()

            else:
                print(formatting["FAIL"] + "This path does not exist")

        else: print(formatting["FAIL"]+"Unknown type, use -typename. Example: -gif")

    else:
        print(formatting["FAIL"]+"No arguments specified")
        welcomePrint()

main()
print("\nExiting")
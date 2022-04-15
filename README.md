# Live wallpaper for Linux XFCE
## A simple script that allows you to play a GIF, video or image sequence on your desktop wallpaper!
**IMPORTANT NOTE:** I'm not sure this will work on every machine. I wrote that script especially for myself. If you discover a bug or know how to improve it, create an issue
<br>
__Make sure you have these programs installed:__
- python
- ffmpeg
- imagemagick

#### Note
I highly recommend to use `performance` CPU governor or the desktop may lag.
You can change the governor by using:
```bash
sudo cpupower frequency-set -g performance
```
You can permanently change the governor by editing file `/etc/default/cpupower`.
Replace `#governor='powersave'` with:
```
governor='performance'
```
**Make sure to remove the `#`!**
## Demonstation
Preview quality may not be accurate with actual wallpaper quality.
<p>
<img src="https://github.com/Wolfyxon/xfce-live-wallpaper/blob/main/github/demos/demo2.gif?raw=true">
<img src="https://github.com/Wolfyxon/xfce-live-wallpaper/blob/main/github/demos/demo1.gif?raw=true">
</p>

# Usage
__IMPORTANT NOTE:__ Paths must be global, example: `/home/username/Pictures/file` not `./file` <br>
`python main.py <type> <path> <frame update wait time (optional, default 0.05)>`
- GIF (Best quality)
```bash
python main.py -gif /home/username/Pictures/mygif.gif
```
- Video (Worst quality)
```bash
python main.py -video /home/username/Videos/myvideo.mp4
```
- Image sequence (slideshow)
```bash
python main.py -sequence /home/username/Pictures/wallpapers/
```
- Last cached animation
```bash
python main.py -cache
```

### How does it work?
First it takes the GIF/video and then converts it to frames.
- Video
```python
os.system("ffmpeg -i "+path+" -vf fps=30 -vf scale=1280:720 cache/frame-%d.png")
```
- GIF
```python
os.system("convert "+path+" -coalesce cache/frame.png")
```
1. The frames are being saved in folder `cahce` that is located in the same directory as the script.
(If you use `-sequence` or `-cache` nothing is being converted)
2. Next, it runs the 2nd script that is used for changing the wallpaper, with path and wait time arguments.
```python
def runFromCache():
    os.system("python " + os.path.abspath("./wallpaper.py") + " " + os.path.abspath("./cache") + " " + str(wait_time))
```
3. Then the `wallpaper.py` keeps changing wallpaper to each frame.
```python
while True:
    time.sleep(wait_time)
    for i in range(len(sequence_files)):
        setWallpaper(path+"/"+"frame-"+str(i)+".png")
        time.sleep(wait_time)
```
(See also `setWallpaper(path)` inside code.)
# Made by Wolfyxon
Enjoy :)
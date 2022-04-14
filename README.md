# Live wallpaper for Linux XFCE
## A simple script that allows you to play a GIF, video or image sequence on your desktop wallpaper!
**IMPORTANT NOTE:** I'm not sure this will work on every machine. I wrote that script especially for myself. If you discover a bug or know how to improve it, create an issue
<br>
__Make sure you have these programs installed:__
- python
- ffmpeg
- imagemagick

## Demonstation
<p>
<img src="https://github.com/Wolfyxon/xfce-live-wallpaper/blob/main/github/demos/demo2.gif?raw=true">
<img src="https://github.com/Wolfyxon/xfce-live-wallpaper/blob/main/github/demos/demo1.gif?raw=true">
</p>

# Usage
__IMPORTANT NOTE:__ Paths must be global, example: `/home/username/Pictures/file` not `./file` <br>
`python main.py <type> <path> <frame update wait time (optional, default 0.05)>`
- GIF:
```
python main.py -gif /home/username/Pictures/mygif.gif
```
- Video
```
python main.py -video /home/username/Videos/myvideo.mp4
```
- Image sequence (slideshow)
```
python main.py -sequence /home/username/Pictures/wallpapers/
```

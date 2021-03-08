from pytube.cli import on_progress
from pytube import YouTube
import os

url = input("Paste your link here :")

try:
    yt = YouTube(url)
    t = yt.streams.filter(only_audio=True)
    t[0].download(output_path="E:/Program Files/yt-mp3/video")

except EOFError as err:
    print(err)

else:
    print("Conversion Success!!")
from pytube import YouTube
import shutil
from os import walk
import os

link = input("Enter your YouTube URL: ")
yt = YouTube(link)

videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("enter the desired format to download")
download_option = int(input("Enter the option: "))


download_video = videos[download_option]

download_video.download()

print("downloaded successfully!")

ROOT_DIR = os.path.abspath(os.curdir)

for (dirpath, dirnames, filenames) in walk("./"):
    for filename in filenames:
        if ".mp4" in filename:
            shutil.move(ROOT_DIR +"/"+ filename, "/Users/kenrickvaz/Downloads/"+ filename)
from pytube import YouTube
from os import walk

import shutil
import os
import humanize


def progress_func(stream, chunk, remaining):
    print(humanize.naturalsize(stream.filesize_approx - remaining) +" of "+ humanize.naturalsize(stream.filesize_approx), end='\r')


link = input("Enter your YouTube URL: ")
yt = YouTube(link, on_progress_callback=progress_func)

videos = yt.streams.order_by('resolution').filter(only_video=True).filter(file_extension='mp4')

video = list(enumerate(videos))


for i in video:
    if i[1].type == "video":
        stream = i[1]
        print(str(i[0]) +"\t|\t"+ stream.mime_type + "\t|\t"+ stream.resolution + "\t|\t"+ humanize.naturalsize(stream.filesize_approx))
    
print("enter the desired format to download")
download_option = int(input("Enter the option: "))


download_video = videos[download_option]

print("downloading >>>>>>>> ")

download_video.download()

print("downloaded successfully!")

ROOT_DIR = os.path.abspath(os.curdir)

for (dirpath, dirnames, filenames) in walk("./"):
    for filename in filenames:
        if ".mp4" in filename:
            shutil.move(ROOT_DIR +"/"+ filename, "/Users/kenrickvaz/Downloads/"+ filename)
            print("moved "+ filename +" to Downloads!")


    
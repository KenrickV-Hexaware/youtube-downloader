from pytube import YouTube
from os import walk
from pathlib import Path

import shutil
import os
import humanize
import instaloader
from os import path

path_to_download_folder = str(os.path.join(Path.home(), "Downloads")) +"/"

def progress_func(stream, chunk, remaining):
    print(humanize.naturalsize(stream.filesize_approx - remaining) +" of "+ humanize.naturalsize(stream.filesize_approx), end='\r')


def downloadYT():
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
                shutil.move(ROOT_DIR +"/"+ filename, path_to_download_folder + filename)
                print("moved "+ filename +" to Downloads!")

    menu()

def downloadIG():
    ig = instaloader.Instaloader()
    dp = input("Enter Insta Username: ")
    
    print("downloading >>>>>>>> ")
    try:
        ig.download_profile(dp, profile_pic_only = True)
        print("downloaded successfully!")

        ROOT_DIR = os.path.abspath(os.curdir)

        print("DOWNLOAD PATH: "+ path_to_download_folder)
        for (dirpath, dirnames, filenames) in walk("./"+ dp +"/"):
            for filename in filenames:
                if ".jpg" in filename:
                    shutil.move(ROOT_DIR +"/"+ dp +"/"+ filename, path_to_download_folder + filename)
                    print("moved "+ filename +" to Downloads!")
    except:
        print("Error downloading profile >>>>")

    if path.exists("./"+ dp +"/"):
        try:
            shutil.rmtree("./"+ dp +"/")
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

    menu()

def menu():
    print("********** Menu **********")
    print("1. Download YouTube Video")
    print("2. Download Insta Profile Pic")
    print("3. Exit")
    print("********** Menu **********\n")

    option = int(input("Enter the option: "))

    if option == 1:
        downloadYT()
    elif option == 2:
        downloadIG()
    elif option == 3:
        print("\n\n********** Thank you **********\n\n")
    else:
        print("Invalid option")
        print("********** Done **********")



menu()
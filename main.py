import numpy as np 
import youtube_dl as yt
from  pytube import Playlist 
import os
import json

links = []
cwd = os.getcwd()
ffmpeg = cwd + "\ffmpeg\bin\ffmpeg.exe"
def singlelink_input(): 
    totalVideos = int (input("Enter the total number of Youtube Videos you want to convert : "))
    for i in range (0,totalVideos):
        link = input (f"Enter Video Link {i+1} : ")
        links.append(link)
        print (links)
    return(links)

def playlist_input():
    link= input ("Enter the Playlist URL : ")
    links = Playlist(link)
    print (links)
    return (links)
    

def downloadVideos(links):
    for i in range (0,len(links)):
        info = open ("info.json" , "x")
        #Download Video Json information
        ydl_opts = {
            'forcetitle'
            'writeinfojson' : info
        }

        with yt.YoutubeDL(ydl_opts) as ydl:
            placehonderarray = []
            placehonderarray.append(links[i])
            ydl.download(placehonderarray)
            
        infoPhrased= json.loads(info) 
        infoPhrasedfile = open ("infoPhrased.json" , "x")
        json.dumps(infoPhrased ,indent=4)
        infoPhrasedfile.write(infoPhrased)

        #Download MP3 
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'flac',
                    'preferredquality': '0',
                }],
        }
        with yt.YoutubeDL(ydl_opts) as ydl:
            placehonderarray = []
            placehonderarray.append(links[i])
            ydl.download(placehonderarray) #Downloads the MP3
        os.remove("dinfoPhrased.json")



def main():
    print ("Welcome to yt2Mp3. Where do you want to download from? \n (1) Download via Links \n (2) Download from playlist \n (3) Read Links from a File \n (4) Exit")
    userinput = int (input("(1), (2), (3)or (4): "))
    downloadPath = input ("Enter your download path i.e (C:/Media/Downlnloads): ")
    match userinput:
        case 1:
            singlelink_input()
        case 2:
            playlist_input()
        case 3:
            print ("Work in progress")
        case 4:
            exit
        case _:
            print ("Input ERROR!!!  PICK 1,2,3 or 4")
            main()

    os.chdir(downloadPath)
    downloadVideos(links=links)
    

main()
#import requests
import yt_dlp
#import urllib3
from yt_dlp import YoutubeDL

#Testing URL = https://youtu.be/SiJie3Z7DG8?si=8sKeL4oRvcs-1C_G #Changed testing url :D WEEZER!

url = input("Enter URL of Video you want to Downlaod: ")
if "https://youtu.be/" not in url:
    url = input("Enter URL of video you want to download")
elif url =="":
    url = input("Enter URL of video you want to download")
else:
    print("")

ydl_opts = {}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

x = 0
for x in range(len(info['formats'])): #Loop prints out all of the formats possible to use
    format = info['formats'][x]
    #print(format.keys())
    print(f"the resolution is: {format['resolution']}")
    print(f"The Format_id is: {format['format_id']}")
    print(f"The Extension is: {format['ext']}")
    print(f"This is option number {x}")
    print("")
    x = x + 1
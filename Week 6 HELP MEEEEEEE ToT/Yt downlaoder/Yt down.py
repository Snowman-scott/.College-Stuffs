import requests
import yt_dlp
import urllib3
from yt_dlp import YoutubeDL

#Testing URL = https://youtu.be/qQzdAsjWGPg?si=IgVwm9oxfSl3Qwml

url = input("Enter URL of Video you want to Downlaod: ")

ydl_opts = {}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)


print(len(info['format']))

format = info['format'][0]

temp = format.keys()

print(temp)
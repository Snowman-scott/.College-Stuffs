#import requests
import yt_dlp
#import urllib3
from yt_dlp import YoutubeDL

#Testing URL = https://youtu.be/SiJie3Z7DG8?si=8sKeL4oRvcs-1C_G #Changed testing url :D WEEZER!

url = input("Enter URL of Video you want to Downlaod: ")
while not url or ("youtu.be/" not in url and "youtube.com/watch?v=" not in url):
    print("Invalid URL. Please Enter a Valid Youtube URL")
    url = input("Enter URL of Video you want to Downlaod: ")

print("Valid URL")

ydl_opts = {}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

x = 0
for x in range(len(info['formats'])): #Loop prints out all of the formats possible to use
    format = info['formats'][x]
    if format['vcodec'] != 'none' and format['acodec'] != 'none':
        print(f"the resolution is: {format['resolution']}")
        print(f"The Format_id is: {format['format_id']}")
        print(f"The Extension is: {format['ext']}")
        print(f"This is option number {x}")
        print("")
        x = x + 1

while True:
    try:
        User_choice = int(input("Enter the number of the option you wnat to download: "))
        if 0 <= User_choice < len(info['formats']):
            break
        else:
            print(f"Invalid choice. Please enter a number between 0 and {len(info['formats']) -1}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Valid choice selected!")

selected_format = info['formats'][User_choice]
format_id = selected_format['format_id']

downlaod_opts = {'format': format_id}

with YoutubeDL(downlaod_opts) as ydl:
    ydl.download([url])
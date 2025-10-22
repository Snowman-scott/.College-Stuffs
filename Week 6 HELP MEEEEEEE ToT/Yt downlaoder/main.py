import os
import yt_dlp
from yt_dlp import YoutubeDL
from Functions import clear_terminal
from Functions import get_browser_choice
from Functions import get_format_choice()
from Functions import filter_formats()



def main():
    print("YouTube Video Downloader")
    print("\nNote: This currently only supports YouTube.")
    print("All audio downloads can be converted to MP3 format.")
    print("FFmpeg is Requiered to convert Audio files to MP3s")
    print("\nThank you for using this tool!\n")

    url = input("\n\n\nEnter URL of Video you want to Download: ")
    while not url or ("youtu.be/" not in url and "youtube.com/watch?v=" not in url):
        print("Invalid URL. Please Enter a Valid Youtube URL")
        url = input("Enter URL of Video you want to Download: ")

    print("\nValid URL")

    # Get browsrr choice
    browser = get_browser_choice()
    if browser:
        ydl_opts = {'cookiesfrombrowser': (browser,)}
    else:
        ydl_opts = {}

    # Extract the video info
    clear_terminal()
    print("Fetching Video information...")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except yt_dlp.utils.DownloadError as e:
        clear_terminal()
        print(f"Error: Could not fetch video information")
        print(f"Details: {e}")
        print("\nPossible reasons:")
        print("- Invalid or unsupported URL")
        print("- Video is private, deleted, or region-restricted")
        print("- Network connection issues")
        if browser:
            print("- Browser cookies couldn't be accessed (try 'Skip' option)")
        return
    except Exception as e:
        clear_terminal()
        print(f"Unexpected error: {e}")
        return


    if not info.get('formats'):
        print("Error: No formats available for this video")
        return
    
    clear_terminal()

    # Get format preferances
    format_type = get_format_choice()
    valid_formats = filter_formats(info['formats'], format_type)

    #I got upto here! Use claud on main account to code! 


# user selects format
while True:
    try:
        User_choice = int(input("Enter the number of the option you want to download: "))
        if 0 <= User_choice < len(valid_formats):
            break
        else:
            print(f"Invalid choice. Please enter a number between 0 and {len(valid_formats) -1}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("\nValid choice selected!\n")

#Downlaod the selected format
selected_format = valid_formats[User_choice]
format_id = selected_format['format_id']

download_opts = {
    'format': format_id,
    'outtmpl':f'{save_path}/%(title)s.%(ext)s',
}

# If audio-only and user wants to, convert to MP3
if Audio_or_both in ['audio', 'a']:
    while True:
        convert = input("Do you want to convert that to an MP3? (y/n)").strip().lower()
        if convert in ['y', 'yes']:
            audio_bitrate = selected_format.get('abr', 192)
            download_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': str(int(audio_bitrate)),

            }]
            print(f"(Audio will be converted to MP3 at {audio_bitrate} kbps)")
        elif convert in ['n','no']:
            break

if browser:
    download_opts['cookiesfrombrowser'] = (browser,)

try:
    clear_terminal()
    with YoutubeDL(download_opts) as ydl:
        ydl.download([url])
        clear_terminal()
    print("\n✓ Download completed successfully!")
except yt_dlp.utils.DownloadError as e:
    clear_terminal()
    print(f"\n✗ Download failed: {e}")
    print("\nPossible reasons:")
    print("- Video may be restricted or unavailable in your region")
    print("- Video may be age-restricted or private")
    print("- URL may be Broken! Try grabbing new URL")
    print("- Yt-dlp may be out of date. Get a new version of application")
except Exception as e:
    clear_terminal()
    print(f"\n✗ Unexpected Error: {e}")
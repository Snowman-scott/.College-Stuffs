import os
import yt_dlp
from yt_dlp import YoutubeDL

def clear_terminal():
    """Clear terminal on Windows, Mac, and Linux"""
    os.system('cls' if os.name == 'nt' else 'clear')

print("This is Currently only a Youtube Video Downloader!")
print("\nI paln to make it accept more sites and resolve issues soon!")
print("\nAll Audio-Only Downloads will be downloaded as an MP3 File Not the format it states when running!")
print("\nI will rework the features another time!")
print("\n\nThank you for using my product!")

url = input("\n\n\nEnter URL of Video you want to Download: ")
while not url or ("youtu.be/" not in url and "youtube.com/watch?v=" not in url):
    print("Invalid URL. Please Enter a Valid Youtube URL")
    url = input("Enter URL of Video you want to Download: ")

print("\nValid URL")

if browser:
    ydl_opts = {'cookiesfrombrowser': (browser,)}
else:
    ydl_opts = {}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

clear_terminal()

# Ask user what they want to download
while True:
    Audio_or_both = input("Do you want to download just the audio or video with audio? (audio/video) ").strip().lower()
    if Audio_or_both in ['audio', 'a']:
        #audio only - filters for audio formats
        valid_formats = []
        for format in info['formats']:
            if format['acodec'] != 'none' and format['vcodec'] == 'none':  # Audio only, no video
                valid_formats.append(format)
        print("\nAvailable audio formats:\n")
        break
    elif Audio_or_both in ['both','b','v','video']:
        #Video with audio - filter for combined formats
        valid_formats = []
        for format in info['formats']:
            if format['vcodec'] != 'none' and format['acodec'] != 'none':
                valid_formats.append(format)
        print("\nAvailable video formats:\n")
        break
    else:
        print("Please enter 'audio' or 'video'")

# Display avalible formats
if not valid_formats:
    print("No valid formats found for your selection. Exiting.")
    exit()

for x in range(len(valid_formats)): #Loop prints out all of the formats possible to use
    format = valid_formats[x]
    print(f"Resolution: {format.get('resolution', 'audio only')}")
    print(f"Format ID: {format['format_id']}")
    print(f"Extension: {format['ext']}")
    if 'abr' in format and format['abr']:
        print(f"Audio bitrate: {format['abr']} kbps")
    print(f"This is option number {x}")
    print("")

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

#Select download location
default_path = os.path.join(os.path.expanduser("~"), "Downloads")
while True:
    save_path = input("Enter download location (Press Enter For Current Dir): ").strip()
    if not save_path:
        save_path = default_path
        print(f"Using default location {save_path}")
        break
    else:
        save_path = os.path.expanduser(save_path) # Handle ~ if user types it

        #check if path exists
        if os.path.exists(save_path):
            if os.path.isdir(save_path):
                print(f"Valid directory: {save_path}")
                break
            else:
                print("Error: That path exists but is not a directory. Please enter a valid directory!")

        else:
            #Ask if the user wants to create it
            create = input(f"Directory '{save_path}' does not exist. Create it? (y/n): ").strip().lower()
            if create in ['y', 'yes']:
                try:
                    os.makedirs(save_path, exist_ok=True)
                    print(f"Created directory: {save_path}")
                    break
                except Exception as e:
                    print(f"Error creating directory: {e}")
                    print("Please try a different path.")
            else:
                print("Please enter a different path.")

clear_terminal()

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
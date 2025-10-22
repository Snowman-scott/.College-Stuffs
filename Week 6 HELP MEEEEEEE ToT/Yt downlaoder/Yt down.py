import os
import yt_dlp
from yt_dlp import YoutubeDL

url = input("Enter URL of Video you want to Download: ")
while not url or ("youtu.be/" not in url and "youtube.com/watch?v=" not in url):
    print("Invalid URL. Please Enter a Valid Youtube URL")
    url = input("Enter URL of Video you want to Download: ")

print("Valid URL")
print("\nTo avoid YouTube bot detection, we'll use your browser's cookies.")
print("Which browser are you using?")
print("1. Chrome")
print("2. Firefox")
print("3. Edge")
print("4. Safari")
print("5. Skip (may not work)")

browser_choice = input("Enter number (1-5): ").strip()
browser_map = {
    '1': 'chrome',
    '2': 'firefox',
    '3': 'edge',
    '4': 'safari',
    '5': None
}

browser = browser_map.get(browser_choice, 'chrome')

if browser:
    ydl_opts = {'cookiesfrombrowser': (browser,)}
else:
    ydl_opts = {}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

# Ask user what they want to download
while True:
    Audio_or_both = input("Do you want to download just the audio or video with audio? (audio/video)").strip().lower()
    if Audio_or_both in ['audio', 'a']:
        #audio only - filters for audio formats
        valid_formats = []
        for format in info['formats']:
            if format['acodec'] != 'none' and format['vcodec'] == 'none':  # Audio only, no video
                valid_formats.append(format)
        print("\nAvailable audio formats:")
        break
    elif Audio_or_both in ['both','b','v','video']:
        #Video with audio - filter for combined formats
        valid_formats = []
        for format in info['formats']:
            if format['vcodec'] != 'none' and format['acodec'] != 'none':
                valid_formats.append(format)
        print("\nAvailable video formats:")
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

print("Valid choice selected!")

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

#Downlaod the selected format
selected_format = valid_formats[User_choice]
format_id = selected_format['format_id']

download_opts = {'format': format_id,
                 'outtmpl':f'{save_path}/%(title)s.%(ext)s',
                 }
if browser:
    download_opts['cookiesfrombrowser'] = (browser,)

try:
    print("\nDownloading video...")
    with YoutubeDL(download_opts) as ydl:
        ydl.download([url])
    print("\n✓ Download completed successfully!")
except yt_dlp.utils.DownloadError as e:
    print(f"\n✗ Download failed: {e}")
    print("\nPossible reasons:")
    print("- Video may be restricted or unavailable in your region")
    print("- Video may be age-restricted or private")
    print("- URL may be Broken! Try grabbing new URL")
    print("- Yt-dlp may be out of date. Get a new version of application")
except Exception as e:
    print(f"\n✗ Unexpected Error: {e}")

# makle it so it can run without user needing yt_dlp on their machine (Idk how ToT Claude can help!)
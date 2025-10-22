import os
import yt_dlp
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
valid_formats = []
for format in info['formats']:
    if format['vcodec'] != 'none' and format['acodec'] != 'none':
        valid_formats.append(format)

for x in range(len(valid_formats)): #Loop prints out all of the formats possible to use
    format = valid_formats[x]
    print(f"the resolution is: {format['resolution']}")
    print(f"The Format_id is: {format['format_id']}")
    print(f"The Extension is: {format['ext']}")
    print(f"This is option number {x}")
    print("")
    x = x + 1

while True:
    try:
        User_choice = int(input("Enter the number of the option you wnat to download: "))
        if 0 <= User_choice < len(valid_formats):
            break
        else:
            print(f"Invalid choice. Please enter a number between 0 and {len(valid_formats) -1}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Valid choice selected!")

default_path = os.path.join(os.path.expanduser("~"), "Downloads")
while True:
    save_path = input("Enter downlaod location (Press Enter For Current Dir): ").strip()
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
                print("Plese enter a differnt path.")

selected_format = valid_formats[User_choice]
format_id = selected_format['format_id']

downlaod_opts = {'format': format_id,
                 'outtmpl':f'{save_path}/%(title)s.%(ext)s'}

try:
    print("\nDownloading video...")
    with YoutubeDL(downlaod_opts) as ydl:
        ydl.download([url])
    print("\n✓ Download completed successfully!")
except yt_dlp.utils.DownloadError as e:
    print(f"\n✗ Download failed: {e}")
    print("\nPossible reassons:")
    print("- Video may be restricted or unavailable in your region")
    print("- Video may be age-restricted or private")
    print("- URL may be Broken! Try grabbing new URL")
    print("- Yt-dlp may be out of date. Get a new version of application")
except Exception as e:
    print(f"\n✗ Unexpected Error: {e}")

# makle it so it can run without user needing yt_dlp on their machine (Idk how ToT Claude can help!)
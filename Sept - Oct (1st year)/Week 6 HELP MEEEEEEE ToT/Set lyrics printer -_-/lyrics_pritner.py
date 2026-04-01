import os
import re
import subprocess
import sys
import time

import requests
import vlc
import yt_dlp

frames = [
    " [========]\n |(|)  (|)|\n ==========",
    " [========]\n |(/)  (/)|\n ==========",
    " [========]\n |(-)  (-)|\n ==========",
    " [========]\n |(\\)  (\\)|\n ==========",
]


def clear_terminal():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def select_track():
    clear_terminal()
    print("===Lyric Printer===")
    search = input("\nEnter the name of a song: ")
    print("\n")

    response = requests.get("https://lrclib.net/api/search", params={"q": search})

    data = response.json()

    for i, item in enumerate(data):
        if item["syncedLyrics"] is not None:
            print(
                f"[{i}] {item['trackName']} - {item['artistName']} ({item['albumName']}) ⏱"
            )
        else:
            print(
                f"[{i}] {item['trackName']} - {item['artistName']} ({item['albumName']})"
            )

    print(
        "\n\n=== For best syncing select a track with the ⏱ Symbol at the end of it's name ==="
    )
    while True:
        try:
            track = int(input("\nSelect track number: "))
            break
        except ValueError:
            print("that is not a track number!")
            continue

    clear_terminal()

    lyrdata = data[track]
    return lyrdata


def lrclib_id(lyrdata):
    print(" ===LRCLib Track Id Is :", lyrdata["id"], " ===")
    time.sleep(2)
    clear_terminal()


def play_tape_animation(duration):
    sys.stdout.write(frames[0] + "\n")
    sys.stdout.flush()

    frame_delay = 0.15
    total_frames = int(duration / frame_delay)

    for i in range(total_frames):
        frame = frames[i % len(frames)]

        sys.stdout.write("\033[3A")

        sys.stdout.write(frame + "\n")
        sys.stdout.flush()

        time.sleep(frame_delay)


def parse_lrc(synclyr):
    results = []
    for line in synclyr.splitlines():
        match = re.match(r"\[(\d+):(\d+\.\d+)\] (.*)", line)
        if match:
            mins = int(match.group(1))
            sec = float(match.group(2))
            total_secs = (mins * 60) + sec
            text = match.group(3)
            results.append((total_secs, text))
    return results


def tidal_search(lyrdata):
    song_name = lyrdata["trackName"]
    artist_name = lyrdata["artistName"]
    album_name = lyrdata["albumName"]
    track_length = lyrdata["duration"]
    best = None
    best_diff = 999
    track_info = requests.get(
        f"https://hund.qqdl.site/search/?s={song_name}&a={artist_name}&al={album_name}&limit=5"
    )

    search_data = track_info.json()["data"]

    for item in search_data["items"]:
        diff = abs(item["duration"] - track_length)
        if diff < best_diff:
            best_diff = diff
            best = item

    if best_diff <= 5:
        song_id = best["id"]
    else:
        song_id = None
    return song_id


def youtube_search(lyrdata):
    song_name = lyrdata["trackName"]
    artist_name = lyrdata["artistName"]
    album_name = lyrdata["albumName"]
    track_length = lyrdata["duration"]
    best = None
    best_diff = 999
    ydl_opts = {"format": "bestaudio", "quiet": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search = f"ytsearch5:{song_name} {artist_name} {album_name}"
        info = ydl.extract_info(search, download=False)
    for entry in info["entries"]:
        diff = abs(entry["duration"] - track_length)
        if diff < best_diff:
            best_diff = diff
            best = entry
    if best_diff <= 5:
        return best["url"]
    else:
        return None


def get_song(song_id):
    if song_id is not None:
        song_request = requests.get(
            f"https://hund.qqdl.site/trackManifests/?id={song_id}"
        )
        song_request_data = song_request.json()["data"]

        return song_request_data["data"]["attributes"]["uri"]
    return None


def main(lyrdata, url):
    if lyrdata["syncedLyrics"] is not None:
        synclyr = lyrdata["syncedLyrics"]
    else:
        plainlyr = lyrdata["plainLyrics"]

    if lyrdata["syncedLyrics"] is not None:
        parsed = parse_lrc(synclyr)
        instance = vlc.Instance(
            "--no-video", "--quiet", "--intf=dummy", "--live-caching=2000"
        )
        player = instance.media_player_new()
        media = instance.media_new(url)
        player.set_media(media)
        player.play()

        if parsed[0][0] > 0:
            play_tape_animation(parsed[0][0])
        else:
            play_tape_animation(2)

        for i, (timestamp, text) in enumerate(parsed):
            while True:
                t = player.get_time()
                if t >= 0 and (t / 1000) >= timestamp + 0.3:
                    break
                time.sleep(0.01)
            if text.strip() == "":
                duration = parsed[i + 1][0] - timestamp
                play_tape_animation(duration)
            else:
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.04)
                print()
    else:
        for line in plainlyr.splitlines():
            if line.strip() == "":
                play_tape_animation(2)
            else:
                delay = max(1.5, len(line) * 0.06)
                for char in line:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.04)
                print()
                time.sleep(delay)


lyrdata = select_track()
lrclib_id(lyrdata)

try:
    song_id = tidal_search(lyrdata)
    url = get_song(song_id)
except Exception:
    url = None

if url is None:
    url = youtube_search(lyrdata)

if url is None:
    clear_terminal()
    print("No sources have the proper song available :<")
else:
    main(lyrdata, url)

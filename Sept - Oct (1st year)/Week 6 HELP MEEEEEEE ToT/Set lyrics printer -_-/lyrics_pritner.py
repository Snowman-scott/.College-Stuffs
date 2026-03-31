import os
import re
import subprocess
import sys
import time

import requests


def clear_terminal():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


frames = [
    " [========]\n |(|)  (|)|\n ==========",
    " [========]\n |(/)  (/)|\n ==========",
    " [========]\n |(-)  (-)|\n ==========",
    " [========]\n |(\\)  (\\)|\n ==========",
]


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
        mins = int(match.group(1))
        sec = float(match.group(2))
        total_secs = (mins * 60) + sec
        text = match.group(3)
        results.append((total_secs, text))
    return results


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
        print(f"[{i}] {item['trackName']} - {item['artistName']} ({item['albumName']})")

print(
    "\n\n=== For best syncing select a track with the ⏱ Symbol at the end of it's name ==="
)
track = int(input("\nSelect track number: "))

clear_terminal()

lyrdata = data[track]

print(" ===LRCLib Track Id Is :", lyrdata["id"], " ===")
time.sleep(2)
clear_terminal()

if lyrdata["syncedLyrics"] is not None:
    synclyr = lyrdata["syncedLyrics"]
else:
    plainlyr = lyrdata["plainLyrics"]

if lyrdata["syncedLyrics"] is not None:
    parsed = parse_lrc(synclyr)
    start = time.time()
    if parsed[0][0] > 0:
        play_tape_animation(parsed[0][0])
    for i, (timestamp, text) in enumerate(parsed):
        time.sleep(max(0, start + timestamp - time.time() - len(text) * 0.04))
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

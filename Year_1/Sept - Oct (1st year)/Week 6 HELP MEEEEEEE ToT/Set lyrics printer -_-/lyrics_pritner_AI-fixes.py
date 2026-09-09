import json
import os
import re
import socket
import subprocess
import sys
import time

import requests

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
    if duration <= 0:
        return

    sys.stdout.write(frames[0] + "\n")
    sys.stdout.flush()

    frame_delay = 0.15
    start_anim = time.time()
    i = 0

    while time.time() - start_anim < duration:
        frame = frames[i % len(frames)]
        sys.stdout.write("\033[3A")
        sys.stdout.write(frame + "\n")
        sys.stdout.flush()

        sleep_time = min(frame_delay, duration - (time.time() - start_anim))
        if sleep_time > 0:
            time.sleep(sleep_time)
        i += 1


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


def get_song(lyrdata):
    song_name = lyrdata["trackName"]
    artist_name = lyrdata["artistName"]
    album_name = lyrdata["albumName"]

    track_info = requests.get(
        f"https://hund.qqdl.site/search/?s={song_name}&a={artist_name}&al={album_name}&limit=5"
    )
    search_data = track_info.json()["data"]
    song_id = search_data["items"][0]["id"]

    song_request = requests.get(f"https://hund.qqdl.site/trackManifests/?id={song_id}")
    song_request_data = song_request.json()["data"]
    url = song_request_data["data"]["attributes"]["uri"]

    return url


def get_mpv_start(process):
    socket_path = "/tmp/mpv-socket"

    while not os.path.exists(socket_path):
        time.sleep(0.01)

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.settimeout(0.01)  # Ultra fast timeout so time.time() doesn't drift

    while True:
        try:
            sock.connect(socket_path)
            break
        except Exception:
            time.sleep(0.01)

    req_id = 1
    buffer = ""

    while True:
        # playback-time factors in audio hardware latency for exact sync!
        prop = "playback-time" if req_id % 2 != 0 else "time-pos"
        req_msg = (
            json.dumps({"command": ["get_property", prop], "request_id": req_id}) + "\n"
        )

        try:
            sock.sendall(req_msg.encode())
        except Exception:
            pass

        while True:
            try:
                chunk = sock.recv(8192).decode("utf-8", errors="ignore")
                if not chunk:
                    break
                buffer += chunk
                if "\n" in chunk:
                    break
            except socket.timeout:
                break

        if "\n" in buffer:
            lines = buffer.split("\n")
            buffer = lines.pop()
            for line in lines:
                if not line.strip():
                    continue
                try:
                    msg = json.loads(line)
                    if msg.get("request_id") == req_id:
                        if (
                            msg.get("error") == "success"
                            and msg.get("data") is not None
                        ):
                            val = float(msg["data"])
                            if val > 0.05:
                                sock.close()
                                return time.time() - val
                except Exception:
                    pass

        req_id += 1
        time.sleep(0.01)


def main(lyrdata, url):
    socket_path = "/tmp/mpv-socket"
    if os.path.exists(socket_path):
        try:
            os.remove(socket_path)
        except Exception:
            pass

    if lyrdata["syncedLyrics"] is not None:
        synclyr = lyrdata["syncedLyrics"]
    else:
        plainlyr = lyrdata["plainLyrics"]

    if lyrdata["syncedLyrics"] is not None:
        parsed = parse_lrc(synclyr)
        process = subprocess.Popen(
            ["mpv", "--no-video", f"--input-ipc-server={socket_path}", url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        start = get_mpv_start(process)

        if parsed and parsed[0][0] > 0:
            target_start = start + parsed[0][0] - (len(parsed[0][1]) * 0.04)
            play_tape_animation(target_start - time.time())

        for i, (timestamp, text) in enumerate(parsed):
            typing_duration = len(text) * 0.04
            target_start_time = start + timestamp - typing_duration

            if text.strip() == "":
                # Wait until the instrumental gap starts before animating
                sleep_duration = target_start_time - time.time()
                if sleep_duration > 0:
                    time.sleep(sleep_duration)

                if i + 1 < len(parsed):
                    # FIX: Deduct the next line's typing time from the animation duration!
                    next_typing_duration = len(parsed[i + 1][1]) * 0.04
                    next_start_time = start + parsed[i + 1][0] - next_typing_duration

                    anim_duration = next_start_time - time.time()
                    if anim_duration > 0:
                        play_tape_animation(anim_duration)
            else:
                sleep_duration = target_start_time - time.time()
                if sleep_duration > 0:
                    time.sleep(sleep_duration)

                # FIX: Dynamically type to ALWAYS finish exactly at the timestamp
                # No more domino effect pushing following lines late!
                finish_time = start + timestamp
                time_left = finish_time - time.time()

                if time_left <= 0:
                    # We overlapped! Print instantly to prevent lagging
                    sys.stdout.write(text + "\n")
                    sys.stdout.flush()
                else:
                    char_delay = time_left / max(1, len(text))
                    type_start = time.time()

                    for idx, char in enumerate(text):
                        sys.stdout.write(char)
                        sys.stdout.flush()

                        expected_char_finish = type_start + (idx + 1) * char_delay
                        sleep_time = expected_char_finish - time.time()
                        if sleep_time > 0:
                            time.sleep(sleep_time)
                    print()
    else:
        for line in plainlyr.splitlines():
            if line.strip() == "":
                play_tape_animation(2)
            else:
                delay = max(1.5, len(line) * 0.06)
                type_start = time.time()
                for idx, char in enumerate(line):
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    expected_time = type_start + (idx + 1) * 0.04
                    sleep_time = expected_time - time.time()
                    if sleep_time > 0:
                        time.sleep(sleep_time)
                print()

                elapsed = time.time() - type_start
                remaining = delay - elapsed
                if remaining > 0:
                    time.sleep(remaining)


lyrdata = select_track()
lrclib_id(lyrdata)
url = get_song(lyrdata)
main(lyrdata, url)

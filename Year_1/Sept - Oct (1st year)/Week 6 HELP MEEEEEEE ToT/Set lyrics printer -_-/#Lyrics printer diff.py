# Lyrics printer diff

import os
import time

os.system("clear")

# ANSI color codes
CYAN = "\033[96m"
BOLD_CYAN = "\033[1m\033[96m"
RESET = "\033[0m"


def print_lyrics():
    # Each tuple contains: (lyric line, delay between characters in seconds)
    lyrics = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the liiiiights ^^", 0.08),
        ("I wanna ro-", 0.08),
        ("I wanna roooooooooOOOock your pyyy", 0.07),
        ("I wanna go...", 0.07),
        ("...I wanna go for a Riiiiiiide :3", 0.06),
        ("Hop in the music and......", 0.06),
        ("RooOOOoock your PYTHON :D", 0.05),
        ("Rock that python..", 0.04),
        ("..come on, come on", 0.04),
        ("Rock that python!! :D", 0.02),
        ("  (Rock your python suka ;)", 0.04),
        ("Rock that python", 0.04),
        ("Rock that python", 0.07),
        ("Make me lose my mind", 0.05),
        ("Rock that python", 0.07),
        ("Rock that python", 0.07),
        ("Rock that python", 0.07),
        ("Come on, come on", 0.06),
        ("Rock that python", 0.07),
        ("Rock that python", 0.07),
        ("Rock that python", 0.07),
        ("Let the rhythm take control", 0.05),
    ]

    for line, char_delay in lyrics:
        # Print each character with a delay
        for char in line:
            print(f"{BOLD_CYAN}{char}{RESET}", end="", flush=True)
            time.sleep(char_delay)

        # Move to next line after completing the current line
        print()  # New line after each lyric

        # Optional: pause between lines
        time.sleep(0.5)


if __name__ == "__main__":
    print_lyrics()

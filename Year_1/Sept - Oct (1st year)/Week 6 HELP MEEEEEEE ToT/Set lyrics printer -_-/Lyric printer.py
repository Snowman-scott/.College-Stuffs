import time
import sys
import os

os.system("clear")

#ANSI color codes
BLUE = '\033[94m'
RESET = '\033[0m'

def print_lyrics():
    #Each tuple contains: (Lyric line, delay between char in seconds)
    lyrics = [
        ("I wanna da-", 0.08 ),
        ("I wanna dance in the liiiiights ^^", 0.08),
        ("I wanna ro-", 0.08),
        ("I wanna roooooooooOOOock your pyyyyython :D", 0.07),
        ("I wanna go...", 0.05),
        ("...I wanna go for a Riiiiiiide :3", 0.06),
        ("Hop in the music and......", 0.06),
        ("RooOOOoock your PYTHON :D", 0.05),
        ("Rock that python..", 0.04),
        ("..come on, come on", 0.04),
        ("Rock that python!! :D", 0.02),
        ("  (Rock your python suka ;)", 0.04),
        ("Rock that python", 0.04),
        ("..Come on, Come on", 0.07),
        ("Rock that python", 0.05),
        ("Rock that python", 0.07),
        ("..Come on, Come on", 0.07),
        ("Rock that python", 0.07),
        ("  (Rock yo' python :3)", 0.06),
        ("Rock that python", 0.07),
        ("Come on, Come on", 0.07),
        ("Rock that python", 0.07), 
    ]

    for line, char_delay in lyrics: 
        #Print each charchter with a delay
        for char in line:
            sys.stdout.write(BLUE + char + RESET)
            sys.stdout.flush()
            time.sleep(char_delay)


        #Moves to next line after compleating current line
        print()

        #Optional paus between line
        time.sleep(0.2)

if __name__ == "__main__":
    print_lyrics()
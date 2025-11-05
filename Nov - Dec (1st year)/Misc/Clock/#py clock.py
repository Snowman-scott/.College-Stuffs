import datetime as dt
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

conf = []

def readconf():
    fh = file.open(".conf.txt", "r")

def hr24Or12():
    
    input("Do you want 12 hr or 24?: ")


def hr12():
    while True:
        cur_time_12hr = time.strftime("%I:%M:%S %p")
        cur_date = time.strftime("%d-%m-%Y")
        clear_screen()
        print(cur_date)
        print(cur_time_12hr)
        time.sleep(1)

def hr12dangerous():
    while True:
        cur_time_12hr = time.strftime("%I:%M:%S %p")
        cur_date = time.strftime("%d-%m-%Y")
        clear_screen()
        print(cur_date)
        print(cur_time_12hr)

def hr24():
    while True:
        cur_time_24hr = time.strftime("%H:%M:%S")
        cur_date = time.strftime("%d-%m-%Y")
        clear_screen()
        print(cur_date)
        print(cur_time_24hr)
        time.sleep(1)

def hr24dangerous():
    while True:
        cur_time_24hr = time.strftime("%H:%M:%S")
        cur_date = time.strftime("%d-%m-%Y")
        clear_screen()
        print(cur_date)
        print(cur_time_24hr)

def main():

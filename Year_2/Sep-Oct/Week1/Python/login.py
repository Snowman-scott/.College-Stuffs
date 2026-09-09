import json
import os
import re
import time

logins = {}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def login():
    try:
        with open("logins.json", "a") as file:
            logins = json.load(file)
    except FileNotFoundError:
        print("ERROR: logins.json not found")

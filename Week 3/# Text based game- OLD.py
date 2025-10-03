# Text based game
import os
import time
import json
import pickle
from datetime import datetime
import re


class Savemanager:
    def __init__(self, base_save_dir="savedata"):
        self.base_save_dir = base_save_dir
        self.ensure_base_directory()

    def ensure_base_directory(self):
        """makes sure base directory exists"""
        if not os.path.exists(self.base_save_dir):
         os.makedirs(self.base_save_dir)
        print(f"Created base save Directory: {self.base_save_dir}")

    def sanitize_filename(self, filename):
        """Reomve invalid charchters from filename"""
        sanitized = re.sub(r'[<>:/\\|?*]', '', filename)
        sanitized = sanitized.replace(' ' , '_')
        return sanitized[:50]
    
    def create_save_folder(self, save_name):
        """Creates new save folder with sanatized name"""
        sanatized_name = self.sanatize_filename(save_name)
        if not sanatized_name:
            sanatized_name = "unnamed_save"
    
        save_path = os.path.join(self.base_save_dir, sanatized_name)

        counter = 1
        original_path = save_path
        while os.path.exists(save_path):
            save_path = f"{original_path}_{counter}"
            counter += 1

        os.makedirs(save_path)
        return save_path
    
    def get_timestamp_filename(self, base_name="gamedata", extension="json"):
        """generate filename with timestamp"""
        timestamp = datetime.now().strftime("%d%m%Y_%H%M")
        return f"{base_name}_{timestamp}.{extension}"

    def save_game_data(self, save_name, game_data):
        """Save game data to subfolde"""
        try:
            save_folder = self.create_save_folder(save_name)
            filename = self.get_timestamp_filename()
            filepath = os.path.join(save_folder, filename)

            with open(filepath, "w") as f:
                json.dump(game_data, f , indent=4)
            
            print(f"Game saved Successfully to: {filepath}")
            return filepath
        except:
            print("Yo")
        


House = { #The "map"
    "The Cold As Conservatory" : {"B" : "Cooking room" , "C" : "Room For Living", "D" : "An Bathroom", "E" : "Stairs!", "Item" : "Batteries and Fuel"},
    "Cooking room" : {"Item" : "Knife"},
    "Room For Living" : {"Item" : "Broken Laptop"},
    "An Bathroom" : {"Item" : "Medical supplies"},
    "stairs!" : {}
}

cl = "The Cold As Conservatory" # current location of the player

inventory = ["Gun"]

os.system("cls")

while True:

    print("Current (See current location) \n\nMove (Move to a different location) \n\nInvo (view your current items in inventory) \n\nPickup (Pick up a new item)")

    move = input("\n\n\nWhat do you want to do?").lower()
    print("\n")
    if move == "current":
        os.system("cls")
        print(f"You are in {cl}\n")

    elif move == "move":
        os.system("cls")
        print("The Cold As Conservatory = A \nCooking room = B \nRoom For Living = C \nAn Bathroom = D \nStairs! = E ")
        print("\nYour current location is: " , cl)
        pm = input("\nWhere would you like to move to?").upper()
        if cl == pm:
            print("invalid move \nYou cannot move to the samce location you are currently at\n")
        elif pm in House[cl]:
            print("you have moved to" , pm)
            time.sleep(1)
            cl = House[cl][pm]
        else:
            print("Invalid input")
    
    elif move == "pickup":
        if "Item" in House[cl]:
            inventory.append(House[cl]["Item"])

    elif move == "invo":
        print("Inventory :\n")
        for Item in inventory:
            print(Item ,"\n")
        print("")
        time.sleep(2)

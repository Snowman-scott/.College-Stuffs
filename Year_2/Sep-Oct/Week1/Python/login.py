import json
import os
import sys

import argon2


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def jsonRead():
    try:
        with open(
            "logins.json",
        ) as file:
            logins = json.load(file)
            return logins
    except FileNotFoundError:
        print("ERROR: logins.json not found")
        sys.exit(1)


def menu():
    options = ["Log In", "Create Account", "quit"]

    while True:
        clearScreen()
        for number, text in enumerate(options, 1):
            print(f"{number}. {text}")

        menu_c = input("\nEnter an option: ")

        try:
            choice = int(menu_c)
        except ValueError:
            input(
                "\nSorry, you did not enter a valid number :<. Press Enter to retry..."
            )
        else:
            if 1 <= choice <= len(options):
                return choice
            input(
                f"\nYour entered choice was not an option \nPlease choose 1 to {len(options)}. \nPress Enter to retry..."
            )


def login(userFeild, passFeild):
    logins = jsonRead()

    ph = argon2.PasswordHasher()

    for i in logins:
        if userFeild == i["username"]:
            try:
                ph.verify(i["password"], passFeild)
            except (argon2.exceptions.VerifyMismatchError, argon2.exceptions.InvalidHash):
                return False
            else:
                return True


def userCheck(user):
    logins = jsonRead()
    for i in logins:
        if user == i["username"]:
            return True
    return False


def accCreate():
    ph = argon2.PasswordHasher()
    while True:
        print("All usernames Must be Lower case, usrnames will automatically be made lowercase by the program \n")
        newuser = input("Enter username for your new account: ").strip().lower()
        clear = userCheck(newuser)
        if clear == True:
            input(
                "\nUsername Already taken, Please try a different username.\nPress Enter to continue. . ."
            )
        elif clear == False:
            break
    while True:
        newPass = input("Enter your password: ")
        confPass = input("Re-Enter your password: ")
        if newPass == confPass:
            hashPass = ph.hash(newPass)
            break
        else:
            print("Your password did not match")
    newEntry = {"username": newuser, "password": hashPass}
    logins = jsonRead()
    logins.append(newEntry)

    with open("logins.json", "w") as f:
        json.dump(logins, f)


def main():
    while True:
        choice = menu()

        if choice == 1:
            usrFeild = input("Enter your username: ").strip().lower()
            pasFeild = input("Enter your password: ")

            backcall = login(usrFeild, pasFeild)

            if backcall == 1:
                print("Login success :3")
            elif backcall == 0:
                print("Username or password was incorrect")
            sys.exit(0)
        elif choice == 2:
            accCreate()
        elif choice == 3:
            sys.exit(0)


main()

# hook it up to a proper database!!!
# (You have the HH postgres Instance live now use it idiot!)

#password Fun 
import os
pswd = 1
user = 1
os.system("cls") # clears terminal

run = input("have you got an account? ").lower()
if run != "yes" : #write to file
    print("cool")

Login = []  # takes file puts it into array to be used in the code
Fh = open("login.txt" , "r")
for line in Fh:
    line = line.strip()
    u,p = line.split(":") # will stip users and passwords
    Login.append([u,p])


print(Login) # Debug

while user != 0:
    username = input("Enter Your username: ")
    if username != Login:
        usr = input("Enter your user name: ")

while pswd != 0: # correct password?
    tps = input("Enter Your Password: ")
    tpsv = input("Confirm your password: ")
    if tps == tpsv:
        with open("Passwords.txt", "a") as file: # remove it Gunna use array
            file.write("\n") #R
            file.write(tps) #R
            file.close #R
            break #R
    else:
        rot = input("Retry Y or N: ")
        if rot == "Y":
            os.system("cls")
        else:
            os.system("cls")
            print("Goodbye")

# Code more :3
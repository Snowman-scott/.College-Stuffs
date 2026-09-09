# enrollment form
import time
import os

cnames = 1 #Correct usernames and passwords
cage = 1 # crrect age
gcse = 1 #correct gcse

while cnames != 0:
    studentfs = input("Enter your First name: ")
    studentls = input("Enter your last name: ")
    time.sleep(1)
    correctname = input(print("Is this the correct First name:", studentfs , "\nAnd is this your Correct Last name: ", studentls))
    if correctname == "yes":
        print("Okay")
        cnames = 0
    else:
        print("Lets retry That")

os.system("cls") # Clears the output

while cage != 0:
    age = int(input("Enter your age: "))
    time.sleep(1)
    corage = input(print("Is this your correct age: ",age))
    if corage == "Yes":
        cage = 0
        if age >= 19:
            print("You getr free Education")
        else:
            print("You will have to apply for a student loan")
    else:
        print("Try again")

os.system("cls") # Clears the output

while gcse != 0:
    eng = input("What did you get on your english GCSE English: ")
    math = input("What did you get in GCSE Maths: ")
    cgce = (input(print("Are these correct? \nEnglish: ",eng ,"\nMaths: ",math)))
    if cgce == "yes":
        gcse = 0
        if eng > 3:
            print("You will have to resit english")
        else:
            print("You dont have to resit English")
        if math > 3:
            print("You have to resit maths")
        else:
            print("you dont have to resit maths")
    else:
        print("Re-enter them here")

os.system("cls") # Clears the output
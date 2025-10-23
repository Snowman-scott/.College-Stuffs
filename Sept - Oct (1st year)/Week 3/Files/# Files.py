#Files
import os

os.system("cls")

Hallo = str(input("what is your naem: "))

with open("Naems.txt", "a") as file:
    file.write(Hallo)
    file.write("\n")


with open("Naems.txt","r") as file:
    content = file.read()

    print(content)
# files demo
file = open("new.txt","w")

file.write("HAIII :3 \n")

with open("new.txt","r") as file:
    content = file.read()
    print(content)

with open("new.txt","r") as file:
    for line in file:
        print(line.strip()) # Strip removes leading/trailing whitespace


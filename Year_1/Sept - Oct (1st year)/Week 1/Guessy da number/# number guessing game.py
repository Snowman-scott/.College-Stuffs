#number guessing game
import os #used
import random #used
import time #Currently Unused

os.system("cls") #clears terminal

games = 0 # resets value for loop

ran_num = random.randint(1,100) # generates a random number

while games != 10: #Game loop
    games = games + 1 # score keeping
    print("guess", games) # users guess info
    ui = int(input("Enter a random number: ")) # user in
    if ui == ran_num: #checkin to see if user guassed it 
        print("You guessed it!")
        games = 10 #changing games to end loop (Could use a break)
    else:
        os.system("cls") # clears terminal
        print("Try again") 
        if ui > ran_num: #is it lower
            print("it is lower")
        elif ui < ran_num: # is it higher
            print("It is Higher")  
            #Retry
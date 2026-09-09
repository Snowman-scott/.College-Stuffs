grid = [["1", "2", "3"],["4","5","6"],["7","8","9"]]

turn = "X"

winner = False

valid = True


'''def wincheck():
    if (grid[0][0] == grid[0][1] == grid[0][2]):
        return True
    elif (grid[1][0] == grid[1][1] == grid[1][2]) == "X":
        return True
    elif (grid[2][0] == grid[2][1] == grid[2][2]) == "X":
        return True
    elif (grid[0][0] == grid[1][0] == grid[2][0]) == "X":
        return True
    elif (grid[0][1] == grid[1][1] == grid[2][1]) == "X":
        return True
    elif (grid[0][2] == grid[1][2] == grid[2][2]) == "X":
        return True
    elif (grid[0][0] == grid[1][1] == [2][2]) == "X":
        return True
    elif (grid[0][2] == grid[1][1] == grid[3][0]) == "X":
        return True
    
    if (grid[0][0] == grid[0][1] == grid[0][2]) == "O":
        return winner == True
    elif (grid[1][0] == grid[1][1] == grid[1][2]) == "O":
        return winner == True
    elif (grid[2][0] == grid[2][1] == grid[2][2]) == "O":
        return winner == True
    elif (grid[0][0] == grid[1][0] == grid[2][0]) == "O":
        return winner == True
    elif (grid[0][1] == grid[1][1] == grid[2][1]) == "O":
        return winner == True
    elif (grid[0][2] == grid[1][2] == grid[2][2]) == "O":
        return winner == True
    elif (grid[0][0] == grid[1][1] == [2][2]) == "O":
        return winner == True
    elif (grid[0][2] == grid[1][1] == grid[3][0]) == "O":
        return winner == True'''



while winner == False:
    Valid = True
    print(grid[0][0], " | ", grid[0][1], " | ", grid[0][2])
    print("---------------")
    print(grid[1][0], " | ", grid[1][1], " | ", grid[1][2])
    print("---------------")
    print(grid[2][0], " | ", grid[2][1], " | ", grid[2][2])
    move = input("Please choose a space: ")
    if move == "1":
        x = 0
        y = 0
    elif move == "2":
        x = 0
        y = 1
    elif move == "3":
        x = 0
        y = 2
    elif move == "4":
        x = 1
        y = 0
    elif move == "5":
        x = 1
        y = 1
    elif move == "6":
        x = 1
        y = 2
    elif move == "7":
        x = 2
        y = 0
    elif move == "8":
        x = 2
        y = 1
    elif move == "9":
        x = 2
        y = 2
    else:
        print("Not a valid move")
        valid = False
    
    if valid != False: 
        if turn == "X":
            grid[x][y] = "X"
            turn = "O"
        else:
            grid[x][y] = "O"
            turn = "X"
    #if wincheck() == False:
        #wincheck()
    
    print(winner)

    if winner == True:
        if turn == "O":
            turn = "X"
            print("Congrats ", turn , " won")
        else:
            if turn == "X":
                turn = "O"
                print("Congrats ", turn , " won")
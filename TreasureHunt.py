# This program is a Treasure Hunt game that searches for treasures based on
# user inputs. If the number a user enters corresponds to the index position
# of a treasure, they receive that treasure. If it corresponds to a number,
# the user is sent to the index position of that number, which if that position
# is a treasure they recieve the treasure but if it's another number, they are
# sent to another index position and so on. The game ends automatically when the
# user is sent out of bounds of the index positions. The user wins one point per
# move between index positions and X points depending on the treasure.

import urllib.request

'''
This function reads the layout of the treasure map and makes it into a list. 
'''
def readFile():
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/treasure.txt")
    html = response.readline().decode('utf-8').split()
    fileList = []
    # ensures the element, '10', is included
    fileList.append(html)
    while len(html) > 0:
        html = response.readline().decode('utf-8').split()
        # creates a list of lists of the data
        fileList.append(html)
    # removes the blank element
    del fileList[-1]
    bigList = []
    # creates a single list where integers and strings are defined as such
    for i in fileList:
        if i[0].isdigit():
            bigList.append(int(i[0]))
        else:
            if len(i) == 1:
                bigList.append(i[0])
            else:
                listVar = i[0] + " " + i[1]
                bigList.append(listVar) 
    return bigList

'''
This function recieves the list of data, asks for user inputs and calculates winnings.
'''
def userInput(file):
    winnings = {}
    print("Welcome to Treasure Hunt!")
    playAgain = 'C'
    while playAgain == 'C':
        theInput = int(input("\nPlease enter a number from 0 to 99: "))
        # start counter at 1 to include the first move as 1 point
        counter = 1
        # raises error if the user enters an invalid input number
        while theInput > 99 or theInput < 0:
            theInput = int(input("\n*Error*\nPlease enter a number from 0 to 99: "))
        # checks if the element is an integer and if so, continues the iterating
        # process until the element isn't an integer (ie, is a string)
        while type(file[theInput]) == int:
            # counter increments for each move
            counter += 1
            check = file[theInput]
            # checks if the index position being moved to is out of bounds
            if check > 99:
                # if the user moves out of bounds they loose everything in their knapsack
                winnings.clear()
                print("\nOut of bounds. You lost everything. Game over.")
                return
            # if the user revists a location, the turn stops without awarding points
            elif file[check] == theInput:
                print("You revisted a node and are not awarded any points.")
                break
            else:
                # moves the value of the integer to the index position of that value
                theInput = file[theInput]
        reward = 0
        # all of the different awards for different treasures found
        if file[theInput] == 'gold':
            reward += 5
        elif file[theInput] == 'silver coins':
            reward += 10
        elif file[theInput] == 'candy':
            reward += 2
        elif file[theInput] == 'cell phone':
            reward += 100
        if type(file[theInput]) == str:
            if file[theInput] in winnings:
                # increments awards of a treasure the user already has
                winnings[file[theInput]] += counter + reward
            else:
                # adds a treasure to the dictionary
                winnings[file[theInput]] = counter + reward
            print("You were awarded ", file[theInput], " and it has been stored in your knapsack")
        playAgain = input("\nWould you like to quit or continue (enter 'Q' to quit, 'C' to continue): ")
        while playAgain != 'Q' and playAgain != 'C':
            playAgain = input("\n*Error*\nPlease enter 'Q' to quit, 'C' to continue: ")
    print("\nTreasure | Amount per treasure")
    for userKey, userValue in winnings.items():
        # prints the final value of their knapsack after the user quits
        print(userKey, "|", userValue)

'''
This function executes the program.
'''
def main():
    file = readFile()
    userInput(file)
main()

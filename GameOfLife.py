#Jonathon Swart
#This program will simulate the Game of Life
#May 31, 2020

#Introduction
print ('''Game of Life
------------''')

#import random
import random

#creates a list with random placements for cells
def createList():
    for x in range(cell_count):
        live = random.randint(1,401)

        while live in numberList:
            live = random.randint(1,401)

        numberList.append(live)
#places the cells randomly in the list based off its random position
def generate():
    pos = 0
    for x in range(20):
        for y in range(20):
            pos += 1
            if pos in numberList:
                gameArray[x][y] = "x"


#prints the randomized cell grid
def showArray():
    for x in range(20):
        for y in range(20):
            print(gameArray[x][y], end= "")

        print()

#Checks how many cells are around it
def CellChecker():
    cell_counter = 0 #counter
    #Checks if cell is in the last place in the list
    if y != 19:
        if gameArray[x][y+1] == "x":   #RIGHT
            cell_counter += 1
    #Checks if cell is last in the list and the last list
    if y >= 0 and y < 19 and x != 19:
        if gameArray[x+1][y+1] == "x": #DOWN RIGHT
            cell_counter += 1
    if y != 0:
        if gameArray[x][y-1] == "x":   #LEFT
            cell_counter += 1
    #Checks if cell is in the last list
    if x != 19:
        if gameArray[x+1][y] == "x":   #DOWN
            cell_counter += 1
    if x < 19 and y > 0:
        if gameArray[x+1][y-1] == "x": #DOWN LEFT
            cell_counter += 1
    if x > 0:
        if gameArray[x-1][y] == "x":   #UP
            cell_counter += 1
    #Checks if cell is in the last place in the list
    if x > 0 and y < 19:
        if gameArray[x-1][y+1] == "x": #UP RIGHT
            cell_counter += 1
    if x > 0 and y > 0:
        if gameArray[x-1][y-1] == "x": #UP LEFT
            cell_counter += 1
            
    return cell_counter

#filter the cells for the next generation
def NextGen(cell_counter):
    if cell_counter < 2:
        cell_change = "-"
    if cell_counter == 2 or cell_counter == 3:
        cell_change = "x"
    if cell_counter > 3:
        cell_change = "-"
        
    return cell_change

gameArray = [['-' for x in range(20)] for y in range(20)]

#Ask user how many cells they would like to start with
cell_count = int(input("\nHow many live cells would you like to start with? "))

#Call Functions to print randomized cell grid
numberList = []
createList()
generate()

again = ''
#counter for each generation of cells
gen_count = 0

#Main Loop
while again == '':
    #Print Generation
    if gen_count == 0:
        print ("\nInitial Generation")
    if gen_count != 0:
        print ("Generation",str(gen_count))
    
    #print grid
    showArray()
    live_cell_counter = 0

    #This list keeps track of what each cell is going to change to
    cell_changeList = []
        
    for x in range(len(gameArray)):
        for y in range(len(gameArray[x])):
            for cell in gameArray[x][y]:
                if cell == "x":
                    live_cell_counter += 1  #count how many live cells there are
                    cell_amount = CellChecker()
                    cell_change = NextGen(cell_amount)
                    #append the position(x and y) and what the cell is changing to into a list
                    cell_changeList.append(x)
                    cell_changeList.append(y)
                    cell_changeList.append(cell_change)
                    
                #Check if dead cells have exactly 3 cells around it          
                if cell == "-":
                    cell_amount = CellChecker()

                    if cell_amount == 3:
                        cell_change = "x"
                        #append the position(x and y) and what the cell is changing to into a list
                        cell_changeList.append(x)
                        cell_changeList.append(y)
                        cell_changeList.append(cell_change)

    #counters to pull x, y, and new cell out of list
    counter1 = 0
    counter2 = 1
    counter3 = 2

    #while loop to go through cellchangeList
    while counter1 != len(cell_changeList):
        x = cell_changeList[counter1]
        y = cell_changeList[counter2]
        cell = cell_changeList[counter3]

        #change cell to its new state
        gameArray[x][y] = cell
        
        counter1 += 3
        counter2 += 3
        counter3 += 3
        
    
    gen_count += 1

    #print amount of live cells
    print ("\nThere are",str(live_cell_counter),"live cells in the grid.")
    #Ask to repeat the program
    again = input("\nPress Enter to See Next Generation: ")
    if again == "N" or again == "n":
        exit            
    

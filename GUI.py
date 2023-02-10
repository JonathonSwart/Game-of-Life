from tkinter import *
import numpy as np

colour = "red"
default_colour = "white"

def main():
    root = Tk()
    root.title("John Conway's Game of Life")
    root.geometry("800x600")

    clicked = []
    # 2D array of all cells
    buttons = []
    for x in range(1,21):
        # Array of cells in a row
        row = []
        for y in range(1, 21):
            b = Button(root, bg=default_colour, activebackground=default_colour, width=2, height=1)
            b.grid(column=x, row=y)
            # Creating the callback with "b" as the deafult parameter below 
            # "freezes" its value pointing to the button created in each run
            # of the loop
            b["command"] = lambda b=b: click(b, clicked)
            row.append(b)
        # Append each row into the array of all buttons
        buttons.append(row)
    
    start_btn = Button(root, text="START", font="Coolvetica", bg="red", fg="white", command=lambda: start(clicked, buttons))
    start_btn.grid(column=6, row= 25, columnspan=10)

    label = Label(root, text="                                                ")
    label.grid(column=0, row= 25)

    root.mainloop()


def locate(cell, array): 
    for row in array:
        for element in row:
            if cell == array[row][element]:
                return "Hello"

    return "Hello World"



def start(clicked, grid):
    cell_counter = 0

    for button in clicked:
        #locate(button, grid)
        print (button)
        

        # if grid[x][y+1] == "x":   #RIGHT
        #     cell_counter += 1
        # if grid[x+1][y+1] == "x": #DOWN RIGHT
        #     cell_counter += 1
        # if grid[x][y-1] == "x":   #LEFT
        #     cell_counter += 1
        # if grid[x+1][y] == "x":   #DOWN
        #     cell_counter += 1
        # if grid[x+1][y-1] == "x": #DOWN LEFT
        #     cell_counter += 1
        # if grid[x-1][y] == "x":   #UP
        #     cell_counter += 1
        # if grid[x-1][y+1] == "x": #UP RIGHT
        #     cell_counter += 1
        # if grid[x-1][y-1] == "x": #UP LEFT
        #     cell_counter += 1
            
    return cell_counter




def click(button, clicked):
    if button in clicked:
        button["bg"] = default_colour
        button["activebackground"] = default_colour
        clicked.remove(button)
    else:
        button["bg"] = colour
        button["activebackground"] = colour
        clicked.append(button)

main()
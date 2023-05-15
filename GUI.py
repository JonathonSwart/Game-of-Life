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


# Returns the index of a button from a 2d array
def locate(cell, array):
    for i, row in enumerate(array):
        if cell in row:
            return (row.index(cell), i)


# The start button has been pressed and the board needs to be updated to
# the next generation of cells
def start(clicked, grid):
    cell_counter = 0
    clicked_cell_pos = []

    for button in clicked:
        # Get all cell positions
        pos = locate(button, grid)
        clicked_cell_pos.append(pos)

    # Check population around each button on the grid
    for row in grid:
        for cell in row:
            counter = 0
            # get button location
            pos = locate(cell, grid)

            # check surrounding cells
            if (pos[0] - 1, pos[1]) in clicked_cell_pos: # Top
                counter += 1
            if (pos[0] - 1, pos[1] + 1) in clicked_cell_pos: # Top Right
                counter += 1
            if (pos[0], pos[1] + 1) in clicked_cell_pos: # Right
                counter += 1
            if (pos[0] + 1, pos[1] + 1) in clicked_cell_pos: # Bottom Right
                counter += 1
            if (pos[0] + 1, pos[1]) in clicked_cell_pos: # Bottom
                counter += 1
            if (pos[0] + 1, pos[1] - 1) in clicked_cell_pos: # Bottom Left
                counter += 1
            if (pos[0], pos[1] - 1) in clicked_cell_pos: # Left
                counter += 1
            if (pos[0] - 1, pos[1] - 1) in clicked_cell_pos: # Top Left
                counter += 1
        
            # If cell has been clicked and has 1 or >=4 surrounding clicked cells then 
            # that cell must be unclicked
            if (counter == 1 or counter >= 4) and (pos in clicked_cell_pos):
                cell["bg"] = default_colour
                cell["activebackground"] = default_colour



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
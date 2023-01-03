from tkinter import *

root = Tk()
root.title("Learn To Code at Codemy.com")
root.geometry("600x600")


def clicked (event) :
    button_number = (int (event.y / 60) * 9) + (1 + int (event.x / 60))
    print (f'You clicked button number {button_number}.')
 
drawCanv = Canvas(width = 541, height = 301, bd = 0)
drawCanv.bind ('<Button-1>', clicked)
 
button_number = 1
for y in range (1, 300, 60) :
    for x in range (1, 540, 60) :
        rectangle = drawCanv.create_rectangle (x, y, x + 60, y + 60,\
            outline = 'black')  
        drawCanv.create_text (x + 25, y + 30, text = button_number)
        button_number += 1
drawCanv.pack ()

root.mainloop()
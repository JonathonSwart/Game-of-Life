from tkinter import *

root = Tk()
root.title("Learn To Code at Codemy.com")

def open():
    top = Toplevel()
    top.title("Second Window")
    lbl = Label(top, text="Hello World")
    lbl.pack()

btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()
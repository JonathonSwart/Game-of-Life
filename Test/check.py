from tkinter import *

root = Tk()
root.title("Learn To Code at Codemy.com")
root.geometry("400x400")

var = StringVar()

c = Checkbutton(root, text="Check This Box", variable=var)
c.pack()

myLabel = Label(root, text=var.get()).pack()

root.mainloop()
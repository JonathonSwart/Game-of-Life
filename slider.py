from tkinter import *

root = Tk()
root.title("Learn To Code at Codemy.com")
root.geometry("400x400")

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="Click Me", command=slide).pack()

root.mainloop()
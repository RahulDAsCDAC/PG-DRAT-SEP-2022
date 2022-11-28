# Creating Radio Button
from tkinter import *

root = Tk()

root.geometry("300x300")

radioVar = IntVar()

def choice():
    selected = {
        1: "WIndows",
        2: "Ubuntu",
        3: "Mac",
    }
    lbl2.config(text = selected[radioVar.get()])
    

lbl = Label(root, text = "Prefered OS:")
lbl.pack()

r1 = Radiobutton(root, text="Windows", variable=radioVar, value=1, command=choice)
r1.pack()
r2 = Radiobutton(root, text="Ubuntu", variable=radioVar, value=2, command=choice)
r2.pack()
r3 = Radiobutton(root, text="Mac", variable=radioVar, value=3, command=choice)
r3.pack()

lbl2 = Label(root)
lbl2.pack()

root.mainloop()
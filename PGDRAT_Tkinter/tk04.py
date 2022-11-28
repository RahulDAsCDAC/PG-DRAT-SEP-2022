# Creating Check Box
from tkinter import *

root = Tk()
root.title("Check Box")
root.geometry("100x100")

def display1():
    print(CheckVar1.get())
def display2():
    print(CheckVar2.get())

CheckVar1 = IntVar()
CheckVar2 = IntVar()
lbl = Label(root, text="preference")
lbl.pack()
c1 = Checkbutton(root, text = "Music", variable = CheckVar1, onvalue=1, offvalue=0, command=display1)  #0001
c2 = Checkbutton(root, text = "Video", variable = CheckVar2, onvalue=2, offvalue=0, command=display2)  #0010

c1.pack()
c2.pack()


root.mainloop()
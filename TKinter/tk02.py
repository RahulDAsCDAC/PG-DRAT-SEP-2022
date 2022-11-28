# Create Buttons
from tkinter import *

root = Tk()

def myClick():
    # print("Clicked")
    txtlabel = Label(root, text="Clicked Me!")
    txtlabel.pack()

myButton = Button(root, text="Click Me!", padx=30, pady=30, command = myClick)
myButton.pack()

root.mainloop()
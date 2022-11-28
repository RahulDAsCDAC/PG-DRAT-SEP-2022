# Create Labels
from tkinter import *

root = Tk()

# Creating a label widget
myLabel1 = Label(root, text = "Hello World")
myLabel2 = Label(root, text = "Welcome")
myLabel3 = Label(root, text = "to")
myLabel4 = Label(root, text = "Kolkata")

# Showing it onto the screen
myLabel1.grid(row=0, column=3)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=1)
myLabel4.grid(row=3, column=2)

root.mainloop()
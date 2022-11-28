# Create Buttons

from tkinter import *

root = Tk()
root.title("Buttons")
root.geometry("300x300")

def clicked():
    #print("True")
    txtLabel =Label(root, text="True")
    txtLabel.pack()

# Create Buttons
myButton1 = Button(root, text="Click me!", padx=20, pady=20, command=clicked)
myButton1.pack()

root.mainloop()
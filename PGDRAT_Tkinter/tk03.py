# Create Entry
from tkinter import *

root = Tk()

# Creating Entry
entry1 = Entry(root, width=50)
entry1.pack()
entry1.insert(0, "Enter your name...")

def save_data():
    hello = "Hello " + entry1.get()
    entry2.delete(0, END)
    entry2.insert(0, hello)

btn1 = Button(root, text="Save", command=save_data)
btn1.pack()

entry2 = Entry(root, width=50)
entry2.pack()

root.mainloop()
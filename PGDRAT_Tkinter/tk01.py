# Ubuntu:
# sudo apt install python3-pip
# sudo apt install python3-tk

from tkinter import *

root = Tk()
root.title("PG-DRAT-GUI")
root.geometry("300x400")

# Creating a label wdget
myLabel1 = Label(root, text="PG-DRAT1")
myLabel2 = Label(root, text="PG-DRAT2")
myLabel3 = Label(root, text="PG-DRAT3")
myLabel4 = Label(root, text="PG-DRAT4")
myLabel5 = Label(root, text="PG-DRAT5")

# Bind the widget to main window
myLabel1.place(x=10,y=20)
myLabel2.place(x=100,y=100)
myLabel3.place(x=200,y=200)
myLabel4.place(x=150,y=200)
myLabel5.place(x=40,y=40)

root.mainloop()

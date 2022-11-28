from tkinter import *
import string, random

from matplotlib.pyplot import title

root = Tk()
root.geometry("300x280")
root.title("Password Generator")

pswStrenght = StringVar()
label = Label(root, textvariable=pswStrenght).pack()
pswStrenght.set("Password Strength")

def selection():
    selection = choice.get()

choice = IntVar()
r1 = Radiobutton(root, text="Poor", variable=choice, value=1, command=selection).pack(anchor=CENTER)
r1 = Radiobutton(root, text="Average", variable=choice, value=2, command=selection).pack(anchor=CENTER)
r1 = Radiobutton(root, text="Advanced", variable=choice, value=3, command=selection).pack(anchor=CENTER)

labelchoice = Label(root).pack()

lenlabel = StringVar()
lenlabel.set("Password Length:")
lentitle = Label(root, textvariable=lenlabel).pack()

val = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()

def callback():
    lsum.config(text=passgen(), font=('Helvetica bold', 12))


passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3).pack()
password = str(callback)

lsum = Label(root, text="", bg="white")
lsum.pack(side=BOTTOM, pady=30)

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()-_+={\}[]\|:;"'<>,.?/"""
advance = poor + average + symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average, val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advance, val.get()))


root.mainloop()
# Create Calculator
from tkinter import *

root = Tk()
root.title("Calcualtor")

entry1 = Entry(root, width=50, borderwidth=5)
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

f_num = ''

def button_click(number):
    #entry1.delet(0, END)
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current) + str(number))

def button_clear():
    entry1.delete(0, END)

def button_add():
    first_number = entry1.get()
    global f_num
    f_num = f"{str(first_number)}+"
    entry1.delete(0,END)

def button_mul():
    first_number = entry1.get()
    global f_num
    f_num = f"{str(first_number)}-"
    entry1.delete(0,END)

def button_sub():
    first_number = entry1.get()
    global f_num
    f_num = f"{str(first_number)}*"
    entry1.delete(0,END)

def button_div():
    first_number = entry1.get()
    global f_num
    f_num = f"{str(first_number)}/"
    entry1.delete(0,END)

def button_equal():
    secon_number = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, eval(f_num + str(secon_number)))

# Define Buttons

button1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_click(0))
buttonAdd = Button(root, text="+", padx=40, pady=20, command=button_add)
buttonSub = Button(root, text="-", padx=40, pady=20, command=button_sub)
buttonMul = Button(root, text="*", padx=40, pady=20, command=button_mul)
buttonDiv = Button(root, text="/", padx=40, pady=20, command=button_div)
buttonEqual = Button(root, text="=", padx=40, pady=20, command=button_equal)
buttonClear = Button(root, text="C", padx=40, pady=20, command=button_clear)

# Put buttons on the screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=1)

buttonAdd.grid(row=3, column=3)
buttonSub.grid(row=2, column=3)
buttonMul.grid(row=1, column=3)
buttonDiv.grid(row=4, column=2)
buttonEqual.grid(row=4, column=3)

buttonClear.grid(row=4, column=0)

root.mainloop()
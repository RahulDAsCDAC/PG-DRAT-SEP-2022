# Image Viewer
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.geometry("1200x600")
root.iconbitmap('C:\\RAHULDAS\\PythonVirtual\\TKinter\\icon\\picture.ico')

my_img = ImageTk.PhotoImage(Image.open("images/jerry.jpg"))
img_label = Label(image=my_img)
img_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
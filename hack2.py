from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("CPU Scheduling")
root.geometry('600x550+550+200')
root.resizable(0, 0)
Tops = Frame(root, height=50, bd=8, relief="flat")
Tops.pack(side=TOP)
Label(Tops, font=('arial', 30, 'bold'),
      text="  Results  ", bd=5).grid(row=0, column=0)

f1 = Frame(root, height=10, width=10, bd=4, relief="flat")
f1.pack(side=TOP)

Label(f1, font=('arial', 15, 'bold'),
      text="  Average Turn around time =  ", bd=5).grid(row=0, column=0)
Label(f1, font=('arial', 15, 'bold'),
      text="  Average Waiting time =  ", bd=5).grid(row=1, column=0)

f2 = Frame(root, height=10, width=100, bd=4, relief="ridge")
f2.pack(side=TOP)

Label(f2, font=('arial', 20, 'bold'),
      text=" Gantt Chart ", bd=5).grid(row=0, column=0)

img = Image.open("adorable-animal-close-up-148182 copy.jpg")
img = img.resize((600, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img)
panel.image = img
panel.pack(side = "bottom")

root.mainloop()



from tkinter import *
root = Tk()
root.title('CPU Scheduling')


x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
frame = Frame(root)

frame.grid(row=0, column=0)
prcs = None
buttons = []


def submit():
    f = open('fl.txt')
    txt = next(f)
    txt = int(txt.strip('\n'))
    f.close()
    flag = False
    if txt == 4 or txt == 5:
        flag = True
    lst = []
    dct = {}
    if flag:
        for i in range(0, len(buttons), 4):
            dct['id'] = buttons[i][0].get()
            dct['at'] = int(buttons[i+1][0].get())
            dct['bt'] = int(buttons[i+2][0].get())
            dct['pr'] = int(buttons[i+3][0].get())
            lst.append(dct)
            dct = {}
    else:
        for i in range(0, len(buttons), 3):
            dct['id'] = buttons[i][0].get()
            dct['at'] = int(buttons[i+1][0].get())
            dct['bt'] = int(buttons[i+2][0].get())
            lst.append(dct)
            dct = {}
    print(lst)


def reset():
    for i in range(len(buttons)):
        buttons[i][0].delete(0, END)


def table_win():
    f = open('fl.txt')
    txt = next(f)
    txt = int(txt.strip('\n'))
    f.close()

    processes = int(prcs.get())
    newwin = Toplevel(root)
    b = Label(newwin, text="Process")
    b.grid(row=0, column=0)
    b = Label(newwin, text="Arrival Time")
    b.grid(row=0, column=1)
    b = Label(newwin, text="Burst Time")
    b.grid(row=0, column=2)
    column = 3
    if txt == 4 or txt == 5:
        column = 4
        b = Label(newwin, text="Priority")
        b.grid(row=0, column=3)
    for i in range(1, processes+1):  # Rows
        for j in range(column):
            tmp = [Entry(newwin, text=""), i, j]
            buttons.append(tmp)
    for i in buttons:
        i[0].grid(row=i[1], column=i[2])

    sub = Button(newwin, text="Submit", command=submit).grid(
        row=processes+2, column=1)
    Reset = Button(newwin, text="Reset", command=reset).grid(
        row=processes+3, column=1)


Label(frame, text="Enter Processes").grid(row=0, column=1)
f = open('fl.txt')
txt = next(f)
txt = int(txt.strip('\n'))
f.close()
if txt == 6:
    Label(frame, text="Enter Time Quantum").grid(row=1, column=1)
    prcs1 = Entry(frame, text="")
    prcs1.grid(row=1, column=2)
prcs = Entry(frame, text="")
prcs.grid(row=0, column=2)


Label(frame, text="").grid(row=2, column=1)
Label(frame, text="").grid(row=3, column=1)
Label(frame, text="").grid(row=4, column=1)
generate = Button(frame, text="Generate", fg="black", font=(
    'arial', 8, 'bold'), width=10, height=1, command=table_win).grid(row=5, column=1)
compute = Button(frame, text="Compute", fg="black", font=(
    'arial', 8, 'bold'), width=10, height=1).grid(row=5, column=2)
exit_button = Button(frame, text="Exit", fg="black", font=(
    'arial', 8, 'bold'), width=10, height=1, command=root.destroy).grid(row=5, column=5)


root.mainloop()

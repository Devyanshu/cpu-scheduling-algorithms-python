
from tkinter import *
root = Tk()
root.title('Main Window')


x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
frame = Frame(root)

frame.grid(row=0, column=0)
prcs = None
buttons = []


def submit():
    lst = []
    for i in buttons:
        lst.append(i[0].get())
    print(lst)


def table_win():  # new window definition
    processes = int(prcs.get())
    newwin = Toplevel(root)
    b = Label(newwin, text="Process")
    b.grid(row=0, column=0)
    b = Label(newwin, text="Arrival Time")
    b.grid(row=0, column=1)
    b = Label(newwin, text="Burst Time")
    b.grid(row=0, column=2)
    '''
    b = Label(newwin, text="Priority")
    b.grid(row=0, column=3)'''
    for i in range(1, processes+1):  # Rows
        for j in range(3):
            tmp = [Entry(newwin, text=""), i, j]
            buttons.append(tmp)
    for i in buttons:
        i[0].grid(row=i[1], column=i[2])

    sub = Button(newwin, text="Submit", command=submit).grid(
        row=processes+2, column=1)
    Reset = Button(newwin, text="Reset").grid(row=processes+3, column=1)


Label(frame, text="Enter Processes").grid(row=0, column=1)
Label(frame, text="Enter Time Quantum").grid(row=1, column=1)
prcs1 = Entry(frame, text="")
prcs = Entry(frame, text="")
prcs.grid(row=0, column=2)
prcs1.grid(row=1, column=2)


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

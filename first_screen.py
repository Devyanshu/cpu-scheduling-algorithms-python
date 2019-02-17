from tkinter import *
from tkinter import messagebox
import second_screen


def main():
    root = Tk()
    root.title("CPU Scheduling")
    root.geometry('500x350+550+200')
    root.resizable(0, 0)
    Tops = Frame(root, height=50, bd=8, relief="raise")
    Tops.pack(side=TOP)
    Label(Tops, font=('arial', 50, 'bold'),
          text="   CPU Scheduling  ", bd=5).grid(row=0, column=0)

    def iExit():
        qExit = messagebox.askyesno("CPU Scheduling", "Do you want to exit?")
        if qExit > 0:
            root.destroy()
            return

    def go():
        f = open('fl.txt', 'w')
        selection = str(v.get())
        f.write(selection)
        f.close()
        root.destroy()
        second_screen.sec_main()

    v = IntVar()
    f1 = Frame(root, height=10, width=10, bd=4, relief="ridge")
    f1.pack(side=TOP)

    f2 = Frame(root, height=10, width=100, bd=4, relief="raise")
    f2.pack(side=RIGHT)

    Label(f1, font=('arial', 15, 'bold'),
          text="Choose a scheduling algorithm:",
          justify=LEFT, padx=20).pack(side=LEFT)

    fcfs_rbtn = Radiobutton(f1, text="FCFS", padx=20,
                            variable=v, value=1).pack(anchor=W)
    sjf_rbtn = Radiobutton(f1, text="SJF", padx=20,
                           variable=v, value=2).pack(anchor=W)
    srtf_rbtn = Radiobutton(f1, text="SRTF", padx=20,
                            variable=v, value=3).pack(anchor=W)
    pp_rbtn = Radiobutton(f1, text="Priority(Preemptive)",
                          padx=20, variable=v, value=4).pack(anchor=W)
    pnp_rbtn = Radiobutton(f1, text="Priority(Non-Preemptive)",
                           padx=20, variable=v, value=5).pack(anchor=W)
    rr_rbtn = Radiobutton(f1, text="Round Robin", padx=20,
                          variable=v, value=6).pack(anchor=W)

    btnGo = Button(f2, text="Go", padx=6, pady=6, bd=2, fg="black", font=(
        'arial', 12, 'bold'), width=14, height=1, command=go).grid(row=0,
                                                                   column=0)
    btnExit = Button(f2, text="Exit", padx=6, pady=6, bd=2, fg="black", font=(
        'arial', 12, 'bold'), width=14, height=1, command=iExit).grid(row=0,
                                                                      column=1)

    root.mainloop()


if __name__ == "__main__":
    print("Run cpu_sheduler.py")

from tkinter import *
from tkinter import ttk

def main():

    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Label(frm, text="column=1").grid(column=1, row=0)
    ttk.Label(frm, text="column=2").grid(column=2, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=0)
    root.mainloop()

if __name__=='__main__':
    main()

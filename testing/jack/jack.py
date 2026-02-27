from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def makeTicBox(col: int, row: int) -> Listbox:
    box = Listbox(root, borderwidth=0, background='white')
    box.grid(column=col, row=row)

    return box

box1 = makeTicBox(0, 0)
box2 = makeTicBox(1, 0)
box3 = makeTicBox(2, 0)
box4 = makeTicBox(0, 1)
box5 = makeTicBox(1, 1)
box6 = makeTicBox(2, 1)
box7 = makeTicBox(0, 2)
box8 = makeTicBox(1, 2)
box9 = makeTicBox(2, 2)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()
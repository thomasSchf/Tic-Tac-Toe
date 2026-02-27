from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def makeTicBox(col: int, row: int) -> Listbox:
    box = Listbox(root, borderwidth=0, background='white')
    box.grid(column=col, row=row)

    return box

boxList = [None] * 3

for row in range(3):
    boxList[row] = [None] * 3

    for col in range(3):
        boxList[row][col] = makeTicBox(col, row)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()
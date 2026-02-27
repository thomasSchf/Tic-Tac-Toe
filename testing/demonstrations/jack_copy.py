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

options = ["X", "O"]
currOption = 0

def turn(event):
    global currOption

    print("hi")
    event.widget["background"] = "red"
    event.widget.insert(END, options[currOption])

    currOption = (currOption + 1) % 2

    # 0 // 2 -> 0 0
    # 1 // 2 -> 0 1
    # 2 // 2 -> 1 0
    # 3 // 2 -> 1 1
    # 4 // 2 -> 2 0

for boxCol in boxList:
    for box in boxCol:
        box.bind("<Button>", turn)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()
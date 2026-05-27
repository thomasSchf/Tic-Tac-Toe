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

#x and o list
xoList = [None] * 3

for row in range(3):
    xoList[row] = [None] * 3

    for col in range(3):
        xoList[row][col] = ""


options = ["X", "O"]
currOption = 0

isPressedFlags = [[False] * len(boxList[0]) for _ in boxList]
print(isPressedFlags)

def turn_generator(row, col):
    def turn(event):
        global currOption

        print(row, col)
        print(isPressedFlags[0])
        print(isPressedFlags[1])
        print(isPressedFlags[2])
    
        if (not isPressedFlags[row][col]):
            event.widget["background"] = "gray"
            event.widget.insert(END, options[currOption])
            currOption = (currOption + 1) % 2

            isPressedFlags[row][col] = True

    return turn

    # 0 // 2 -> 0 0
    # 1 // 2 -> 0 1
    # 2 // 2 -> 1 0
    # 3 // 2 -> 1 1
    # 4 // 2 -> 2 0

for row, boxCol in enumerate(boxList):
    for col, box in enumerate(boxCol):
        box.bind("<Button>", turn_generator(row, col))
        print("hi")
       

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()
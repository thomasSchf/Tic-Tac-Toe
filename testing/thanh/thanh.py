from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def makeTicBox(col: int, row: int) -> Listbox:
    box = Listbox(root, borderwidth=0, background='white')
    box.grid(column=col, row=row)
    box.row = row
    box.col = col
    box.isPressed = False
    box.player = ""

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
    
    if(event.widget.isPressed == False):
        event.widget.isPressed = True
        event.widget["background"] = "mediumseagreen"
        
        player = options[currOption]

        event.widget.insert(END, player)
        event.widget.player = player


        currOption = (currOption + 1) % 2

        if (winCon(player, event.widget.row, event.widget.col) == True):
            messagebox.showinfo("Nice breh", f"{player} is the winner")

        #messagebox.showinfo("Game Concluded", f"{options[currOption]} is the winner.")
        #messagebox.showerror("Hold on!", f"{options[currOption]} must be empty")


for boxCol in boxList:
    for box in boxCol:
        box.bind("<Button>", turn)

def winCon(player: str, row: int, col: int) -> bool:
    if ((row == 0 and col == 0) or (row == 1 and col == 1) or (row == 2 and col == 2)):
        if (diagonalRight(player) == True):
            return True

    if ((row == 0 and col == 2) or (row == 1 and col == 1) or (row == 2 and col == 0)):
        if (diagonalLeft(player) == True):
            return True
        
    if (down(player, col) == True):
        return True

    if (right(player, row) == True):
        return True

    print("No winCon")
    return False

def diagonalRight(player: str) -> bool:
    for i in range(3):
        if (boxList[i][i].player != player): 
            print("drBox")
            return False
    return True

def diagonalLeft(player: str) -> bool:
    for i in range(3):
        if (boxList[i][i].player != player): 
            print("drBox")
            return False
    return True

def down(player: str, col: int) -> bool:
    for i in range(3):
        if (boxList[i][col].player != player): 
            print("drBox")
            return False
    return True

def right(player: str, row: int) -> bool:
    for i in range(3):
        if (boxList[row][i].player != player): 
            print("drBox")
            return False
    return True


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()
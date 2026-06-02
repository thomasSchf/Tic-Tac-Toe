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
    box.symbol = ""

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
        event.widget["background"] = "gray"

        symbol = options[currOption]
        event.widget.insert(END, symbol)
        event.widget.symbol = symbol

        currOption = (currOption + 1) % 2

        if(checkWin(symbol, event.widget.row, event.widget.col) == True):
            messagebox.showinfo("Congrats!", f"{symbol} has won!")
            reset()

for boxCol in boxList:
    for box in boxCol:
        box.bind("<Button>", turn)
        

# Checks if the board is in a win configuration     
def checkWin(symbol: str, row: int, col: int) -> bool:
    #if [0][0], [1][1], or [2][2] check diagRight
    if((row == 0 and col == 0) or (row == 1 and col == 1) or (row == 2 and col == 2)):
        if(diagonalRight(symbol) == True):
            return True

    #if [0][2], [1][1], or [2][0] check diagLeft
    if((row == 0 and col == 2) or (row == 1 and col == 1) or (row == 2 and col == 0)):
        if(diagonalLeft(symbol) == True):
            return True
    
    if(down(symbol, col) == True):
        return True
    if(right(symbol, row) == True):
        return True

    print("checkWin returned false")
    return False

# Checks if the right facing diagonal has three of the same symbols
def diagonalRight(symbol: str) -> bool:
    for index in range(3):
        if(boxList[index][index].symbol != symbol):
            return False
    return True

# Checks if the left facing diagonal has three of the same symbols
#Note: probably will be changed to be more general in the future, currently just like this to make the game work 
def diagonalLeft(symbol: str) -> bool:
    verdict = False

    if((boxList[0][2].symbol == symbol) and (boxList[1][1].symbol == symbol) and (boxList[2][0].symbol == symbol)):
        verdict = True
    return verdict

# Checks if a column has three of the same symbols in a row
def down(symbol: str, col: int) -> bool:
    for i in range(3):
        if(boxList[i][col].symbol != symbol):
            return False
    return True

# Checks if a row has three of the same symbols in a row 
def right(symbol: str, row: int) -> bool:
    for i in range(3):
        if(boxList[row][i].symbol != symbol):
            return False
    return True

# Resets the board for a new game
def reset():
    for row in range(3):
        boxList[row] = [None] * 3

        for col in range(3):
            boxList[row][col] = makeTicBox(col, row)

    for boxCol in boxList:
        for box in boxCol:
            box.bind("<Button>", turn)
       

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()
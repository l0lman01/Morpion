from tkinter import *

fn = Tk()
fn.title("morpion en python")

x_win=0
o_win=0
x_turn= True
gameOver= False

def newGame():
    global x_turn, gameOver

    b1["text"] = ""
    b2["text"] = ""
    b3["text"] = ""
    b4["text"] = ""
    b5["text"] = ""
    b6["text"] = ""
    b7["text"] = ""
    b8["text"] = ""
    b9["text"] = ""

    b1["bg"] = "white"
    b2["bg"] = "white"
    b3["bg"] = "white"
    b4["bg"] = "white"
    b5["bg"] = "white"
    b6["bg"] = "white"
    b7["bg"] = "white"
    b8["bg"] = "white"
    b9["bg"] = "white"

    x_turn = True
    tour["text"] = "tour de X"
    gameOver = False

def checkGame(x_turn):
    if(x_turn):
        check = "X"
    else:
        check = "O"
        
    # 3 ligne
    if(b1["text"] == b2["text"] == b3["text"] == check):
        return b1, b2, b3
    if(b4["text"] == b5["text"] == b6["text"] == check):
        return b4, b5, b6
    if(b7["text"] == b8["text"] == b9["text"] == check):
        return b7, b8, b9

    #3 colonne
    if(b1["text"] == b4["text"] == b7["text"] == check):
        return b1, b4, b7
    if(b2["text"] == b5["text"] == b8["text"] == check):
        return b2, b5, b8
    if(b3["text"] == b6["text"] == b9["text"] == check):
        return b3, b6, b9

    #2 diagonales
    if(b1["text"] == b5["text"] == b9["text"] == check):
        return b1, b5, b9
    if(b3["text"] == b5["text"] == b7["text"] == check):
        return b3, b5, b7

    return None


def click(button):
    global x_turn, gameOver, x_win, o_win
    if(button["text"] != "" or gameOver):
        print("tie")
        return
    button["text"] = "X" if x_turn else "O"
    b = checkGame(x_turn)
    if(b != None):
        b[0]["bg"] = "green"
        b[1]["bg"] = "green"
        b[2]["bg"] = "green"

        if(x_turn):
            tour["text"] = "X win"
            x_win += 1
        else:
            tour["text"] = "O win"
            o_win += 1
        tour["text"] = "X:{} O:{}".format(x_win, o_win)
        gameOver = True
        return
    else:
        #print("tie")
        pass
    x_turn = not x_turn
    tour["text"] = "tour de X" if x_turn else "tour de O"





newGameBtn = Button(text="nouvelle game", command=newGame)
tour = Label(text="tour de X")
score = Label(text="X:{} O:{}".format(x_win, o_win))

newGameBtn.grid(row=0, column=0)
tour.grid(row=0, column=1)
score.grid(row=0, column=2)


b1 = Button(width= 20, height=10, bg="white", command=lambda: click(b1))
b2 = Button(width= 20, height=10, bg="white", command=lambda: click(b2))
b3 = Button(width= 20, height=10, bg="white", command=lambda: click(b3))

b4 = Button(width= 20, height=10, bg="white", command=lambda: click(b4))
b5 = Button(width= 20, height=10, bg="white", command=lambda: click(b5))
b6 = Button(width= 20, height=10, bg="white", command=lambda: click(b6))

b7 = Button(width= 20, height=10, bg="white", command=lambda: click(b7))
b8 = Button(width= 20, height=10, bg="white", command=lambda: click(b8))
b9 = Button(width= 20, height=10, bg="white", command=lambda: click(b9))

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)


fn.mainloop()
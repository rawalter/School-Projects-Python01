#Exercise: 9.6
#By: Robert A. Walters
#Created on: 3/16/16
#Program Description:
from tkinter import * # Import tkinter
from random import randint

class Board:
    def __init__(self):
        window = Tk() # Create a window
        window.title("TicTacToe") # Set a title
        
        imageX = PhotoImage(file = "image/x.gif")
        imageO = PhotoImage(file = "image/o.gif")
        
        for i in range(3):
            frame = Frame(window)
            frame.pack()
            for j in range(3):
                label = Label(frame, image = imageX if randint(0, 1) == 0 else imageO )
                label.pack(side = LEFT)
        
        window.mainloop() # Create an event loop

Board()
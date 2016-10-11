#!/usr/bin/python3.4

#Exercise: 9.5
#By: Robert A. Walters
#Created on: 3/25/16
#Program Description:
from tkinter import *

class ChessBoard:
    def __init__(self):
        window =Tk()
        window.title("Chessboard") # Set a title
        
        self.canvas = Canvas(window, width= 800, height = 800, bg = "white")
        self.canvas.pack()
        
        for r in range(0,8):
            for c in range(0,8):
                if (r+c)%2 !=0:
                    self.rectangle(r*100,c*100,(r+1)*100,(c+1)*100,"black")
                    
        window.mainloop()
    def rectangle(self,x1,y1,x2,y2,color):
        self.canvas.create_rectangle(x1,y1,x2,y2, fill=color)
ChessBoard()
#Thanks to Aaron Gudrian
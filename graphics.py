"""
Graphical User Interface Module
"""

# Gui Interface Module
from Tkinter import *


"""
    draw takes in a canvas object and board type,
    and renders the board onto the given canvas using Tkinter GUI
    """
def draw (canvas,board):
    
    canvas.delete("all")    
    
    ch = 500
    cw = 500    
    
    xs_orig = PhotoImage(file='./ximg.gif')
    os_orig = PhotoImage(file='./oimg.gif')
    xs = xs_orig.subsample(2,2)
    os = os_orig.subsample(2,2)
    
    for i in range(1,3):
        canvas.create_rectangle(i*cw/3-1,0,i*cw/3-1,ch, fill="black")
    
    for i in range(1,3):
        canvas.create_rectangle(0,i*cw/3-1,cw,i*cw/3-1, fill="black")          
    
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 'x'):
                canvas.create_image(cw*(j+1)/3-cw/6, ch*(i+1)/3-ch/6, image=xs)
            if (board[i][j] == 'o'):
                canvas.create_image(cw*(j+1)/3-cw/6, ch*(i+1)/3-ch/6, image=os)
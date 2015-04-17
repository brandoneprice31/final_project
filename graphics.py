
# Gui Interface Module
from Tkinter import *
import numpy as np

def draw (board):
    root = Tk()
    
    root.title('Tic Tac Toe')
    root.geometry('500x500')
    
    cw = 500
    ch = 500
    c = Canvas(root, width=cw, height=ch)
    c.pack()
    
    xs_orig = PhotoImage(file='./ximg.gif')
    os_orig = PhotoImage(file='./oimg.gif')
    xs = xs_orig.subsample(2,2)
    os = os_orig.subsample(2,2)
    
    for i in range(1,3):
        c.create_rectangle(i*cw/3-1,0,i*cw/3-1,ch, fill="black")
    
    for i in range(1,3):
        c.create_rectangle(0,i*cw/3-1,cw,i*cw/3-1, fill="black")          
    
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 'x'):
                c.create_image(cw*(j+1)/3-cw/6, ch*(i+1)/3-ch/6, image=xs)
            if (board[i][j] == 'o'):
                c.create_image(cw*(j+1)/3-cw/6, ch*(i+1)/3-ch/6, image=os)       
    
    mainloop()

b1 = np.array([['x','x','x'],['_','_','o'],['_','_','x']])
draw(b1)

"""
Tic Tac Toe Program
"""


"""
import modules
"""
from Tkinter import *
import initializer as init
#-----------------------------------------------------------------------------

"""
initialize board, player, switch_player fcn, Window and Canvas
"""

player = 'x'

# function that changes the player
def switch_player(p):
    if (p == 'x'):
        return 'o'
    else:
        return 'x'

board = [['_','_','_'],['_','_','_'],['_','_','_']]
W = Tk()

W.title('Tic Tac Toe')
W.geometry('500x500')

# draw canvas onto window
cw = 500
ch = 500
C = Canvas(W, width=cw, height=ch)

# draw lines
for i in range(1,3):
    C.create_rectangle(i*cw/3-1,0,i*cw/3-1,ch, fill="black")
    
for i in range(1,3):
    C.create_rectangle(0,i*cw/3-1,cw,i*cw/3-1, fill="black")          
#-----------------------------------------------------------------------------

"""
define draw function
"""

# initialize x and o image
xs_orig = PhotoImage(file='./ximg.gif')
os_orig = PhotoImage(file='./oimg.gif')
xs = xs_orig.subsample(2,2)
os = os_orig.subsample(2,2)

def draw(b):
    for i in range(3):
        for j in range(3):
            if (b[i][j] == 'x'):
                C.create_image(cw*(j+1)/3-cw/6, ch*(i+1)/3-ch/6, image=xs)
            if (b[i][j] == 'o'):
                C.create_image(cw*(j+1)/3-cw/6, ch*(i+1)/3-ch/6, image=os)
#-----------------------------------------------------------------------------

"""
Add Click Listener
"""

# define click_handler for handling click events
def clicked(event):

    if (0 <= event.y < ch/3):
        i = 0
    if (ch/3 <= event.y < ch*2/3):
        i = 1
    if (ch*2/3 <= event.y <= ch):
        i = 2
    if (0 <= event.x < cw/3):
        j = 0
    if (cw/3 <= event.x < cw*2/3):
        j = 1
    if (cw*2/3 <= event.x <= cw):
        j = 2
    
    global player    
    
    board[i][j] = player
    player = switch_player(player)
    draw(board)

C.bind("<Button-1>", clicked)
C.pack()

W.mainloop()
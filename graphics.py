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

player = init.first_player()

board = init.new()
W = Tk()

W.title('Tic Tac Toe')
W.geometry('500x500')

# draw canvas onto window
cw = 500
ch = 500
C = Canvas(W, width=cw, height=ch)

# draw lines fuction
def draw_lines ():
    for i in range(1,3):
        C.create_rectangle(i*cw/3-1,0,i*cw/3-1,ch, fill="black")
        
    for i in range(1,3):
        C.create_rectangle(0,i*cw/3-1,cw,i*cw/3-1, fill="black")   

draw_lines()


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
new_game handler function
"""

# function that starts new_game            
def new_game(event):
    C.delete('all')
    global board
    board = init.new()
    global player
    player = init.first_player()
    draw_lines()
    draw(board)
    play_game()

       
#-----------------------------------------------------------------------------
"""
def Play Game Function
"""

def play_game ():
    # define click_handler for handling click events
    def clicked(event):
    
        # pinpoint which section was clicked
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
        
        # check if move is valid   
        global board    
        if(init.valid(board,(i,j))):
        
            # add new move to board
            global player    
            board = init.next_state(board,(i,j),player)
            
            # draw new board
            draw(board)    
            
            # check game states
            game_state = init.eval(board,player)
            
            # somebody won
            if (game_state == 'win'):
                C.create_rectangle(100,100,500-100,500-100, fill="white")
                if (player=='x'):
                    message = 'X Wins!'
                else:
                    message = 'O Wins!'
                C.create_text(500/2,500/2,text=message,font=('Purisa',32))
                C.bind("<Button-1>",new_game)
                
            # Cats game
            if (game_state == 'tie'):
                C.create_rectangle(100,100,500-100,500-100, fill="white")
                C.create_text(500/2,500/2,text='Tie Game!',font=('Purisa',32))
                C.bind("<Button-1>",new_game)
            
            # game continues
            else:   
                # switch player
                player = init.opponent(player) 
    
    C.bind("<Button-1>", clicked)
    C.pack()
    
    W.mainloop()
play_game()
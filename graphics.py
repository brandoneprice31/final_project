"""
CS 51

Tic Tac Toe Program

by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
"""


#-----------------------------------------------------------------------------
"""
import modules
"""

from Tkinter import *
import initializer as init
import tables as tables
import learning as comp
#import tables as T
from time import sleep


#-----------------------------------------------------------------------------
"""
def start_game function which plays a game given a game_type
"""

def start_game (game_type):
    
    #--------------------------------------------------------------------------
    """
    initialize Canvas
    """
    
    # draw canvas onto window
    cw = 500
    ch = 500
    C = Canvas(W, width=cw, height=ch)
    
    
    #--------------------------------------------------------------------------
    """
    define draw_lines function which draws the lines onto the board
    """
    
    # draw lines fuction
    def draw_lines ():
        for i in range(1,3):
            C.create_rectangle(i*cw/3-1,0,i*cw/3-1,ch, fill="black")
            
        for i in range(1,3):
            C.create_rectangle(0,i*cw/3-1,cw,i*cw/3-1, fill="black")   
    
    
    #--------------------------------------------------------------------------
    """
    define draw function which draws the current board
    """
    
    # initialize and resize x and o image
    xs_orig = PhotoImage(file='./ximg.gif')
    os_orig = PhotoImage(file='./oimg.gif')
    xs = xs_orig.subsample(2,2)
    os = os_orig.subsample(2,2)
    
    def draw((i,j),player):
        if (player == 'x'):
            C.create_image(cw*(j+1)/3-cw/6, ch*(i+1)/3-ch/6, image=xs)
        if (player == 'o'):
            C.create_image(cw*(j+1)/3-cw/6, ch*(i+1)/3-ch/6, image=os)
                    
           
   #--------------------------------------------------------------------------
    """
    define end game function which draws the end screen
    """
    
    def end_game (game_type, end_type, player):
        # draw white rectangle
        C.create_rectangle(100,100,500-100,500-100, fill="white")
        if (end_type == 'win'):
            if (player=='x'):
                message = 'X Wins!'
            else:
                message = 'O Wins!'
        else:
            message = 'Tie Game!'
        C.create_text(500/2,500/2,text=message,font=('Purisa',32))
        if (game_type == 'hvh'):
            C.bind("<Button-1>",new_hvh_game)
        elif (game_type == 'hvc'):
            C.bind("<Button-1>",new_hvc_game)
        elif (game_type == 'cvc'):
            C.bind("<Button-1>",new_cvc_game)
    
           
    #--------------------------------------------------------------------------
    """
    def add_move_listener which adds a listener for a move event
    """
    def human_move(event):
    
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
            board = init.next_state((board,player),(i,j))[0]
            
            # draw new board
            draw((i,j),player)
            
            # check game states
            game_state = init.eval((board,player))
            
            # game over
            if (game_state != 'continue'):
                end_game(game_type,game_state,player)
            
            else:
                player = init.opponent(player)
                W.event_generate("<<foo>>")
    
    
    #--------------------------------------------------------------------------
    """
    def add_move_listener which adds a listener for a move event
    """
    def comp_move(event):
        
        # get the next move from the computer
        # EDIT FROM PETER
        stateKey = tables.makeKey((board,player))
        if stateKey not in tables.qTable:
            tables.addKey(stateKey,tables.qTable)
        next_move = comp.chooseMove((board,player), tables.qTable)
        
        #implement the next move
        global board
        global player
        board = init.next_state((board,player),next_move)[0]
        draw(next_move,player)
        
        # check game states
        game_state = init.eval((board,player))
        
        if (game_state != 'continue'):
            end_game(game_type,game_state,player)
        
        else:
            player = init.opponent(player)


    #--------------------------------------------------------------------------
    """
    new_hvh_game handler function
    """
    
    # function that starts new game involving humans            
    def new_hvh_game(event):
        C.delete('all')
        global board
        board = init.new()
        global player
        player = init.random_player()
        draw_lines()
        
        C.bind("<Button-1>", human_move)
        C.pack()        
        W.mainloop()
        
        
    #--------------------------------------------------------------------------
    """
    new_human_game handler function
    """
    
    # function that starts new game involving human and computer          
    def new_hvc_game(event):
        C.delete('all')
        global board
        board = init.new()
        global player
        player = init.random_player()
        draw_lines()
        
        C.bind("<Button-1>", human_move)
        W.bind("<<foo>>", comp_move)
        C.pack()
        W.mainloop()
        
        
    #--------------------------------------------------------------------------
    """
    new_cvc_game  function
    """
    
    # function that starts new game involving computers          
    def new_cvc_game(event):
        C.delete('all')
        global board
        board = init.new()
        global player
        player = init.random_player()
        draw_lines()
        
        while (init.eval((board,player)) == 'continue'):
            comp_move("automatic")
        
        C.pack()
        W.mainloop()

    #--------------------------------------------------------------------------
    """
    play a new game
    """
    
    if (game_type == 'hvh'):
        new_hvh_game('first')
    elif (game_type == 'hvc'):
        new_hvc_game('first')
    else:
        new_cvc_game('first')
    
    
#-----------------------------------------------------------------------------
"""
initialize Window and Main Menu
"""
W = Tk()

w = 500
h = 500

sw = W.winfo_screenwidth()
sh = W.winfo_screenheight()

window_x = sw/2 - w/2
window_y = sh/2 - h/2

W.title('Tic Tac Toe')
W.geometry('%dx%d+%d+%d'%(w,h,window_x,window_y))
W.resizable(width=FALSE, height=FALSE)

# define game type functions
def hvh ():
    humvhum.pack_forget()
    humvcomp.pack_forget()
    compvcomp.pack_forget()
    title.pack_forget()
    credits.pack_forget()
    start_game('hvh')
    
def hvc ():
    humvhum.pack_forget()
    humvcomp.pack_forget()
    compvcomp.pack_forget()
    title.pack_forget()
    credits.pack_forget()
    start_game('hvc')
    
def cvc ():
    humvhum.pack_forget()
    humvcomp.pack_forget()
    compvcomp.pack_forget()
    title.pack_forget()
    credits.pack_forget()
    start_game('cvc')

# create buttons
humvhum = Button(master = W, text = 'Human vs. Human', command = hvh,
                 pady = 0.02*h, font = ('Purisa', 32*sh/900))
humvcomp = Button(master = W, text = 'Human vs. Computer', command = hvc, 
                  pady = 0.02*h, font = ('Purisa', 32*sh/900))
compvcomp = Button(master = W, text = 'Computer vs. Computer', command = cvc,
                   pady = 0.02*h, font = ('Purisa', 32*sh/900))

# create title and credits
title = Label(master = W, text = 'Tic Tac Toe',
              font = ('Cambria', 64*sh/900, 'bold'))
credits = Label(master = W,
                text = 'by Vincent Chow, Stephen Albro, \
Peter Hickman, & Brandon Price',
                font = ('Cambria', 12))

# display buttons, title, and credits
title.pack(pady=0.06*h)
humvhum.pack(fill=X, pady=0.04*h)
humvcomp.pack(fill=X, pady=0.04*h)
compvcomp.pack(fill=X, pady=0.04*h)
credits.pack(pady=0.02*h)

W.mainloop()
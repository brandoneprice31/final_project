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
import learning as comp
#import tables as T


#-----------------------------------------------------------------------------
"""
def start_game function which plays a game given a game_type
"""

def start_game (game_type):
    #--------------------------------------------------------------------------
    """
    initialize board, player, and Canvas
    """
    
    player = init.random_player()
    
    board = init.new()
    
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
    
    
    #--------------------------------------------------------------------------
    """
    define draw function which draws the current board
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
    
           
    #--------------------------------------------------------------------------
    """
    def add_move_listener which adds a listener for a move event
    """
    
    def add_move_listener ():
        # define click_handler for handling click events
        def move(event):
        
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
                draw(board)    
                
                # check game states
                game_state = init.eval((board,player))
                
                # somebody won
                if (game_state == 'win'):
                    C.create_rectangle(100,100,500-100,500-100, fill="white")
                    if (player=='x'):
                        message = 'X Wins!'
                    else:
                        message = 'O Wins!'
                    C.create_text(500/2,500/2,text=message,font=('Purisa',32))
                    C.bind("<Button-1>",new_human_game)
                    
                # cats game
                elif (game_state == 'tie'):
                    C.create_rectangle(100,100,500-100,500-100, fill="white")
                    C.create_text(500/2,500/2,text='Tie Game!',font=('Purisa',
                                                                     32))
                    C.bind("<Button-1>",new_human_game)
                
                # game continues
                else:   
                    # switch player
                    player = init.opponent(player)
                    
                    
                    # if its a hum vs comp game_type
                    if (game_type == 'hvc'):
                        # pause the program
                        
                        # get the next move from the computer
                        next_move = comp.chooseMove((board,player), "")
                        #implement the next move
                        board = init.next_state((board,player),next_move)[0]
                        draw(board)
                        
                        # check game states
                        game_state = init.eval((board,player))
                        
                        # somebody won
                        if (game_state == 'win'):
                            C.create_rectangle(100,100,500-100,500-100, fill="white")
                            if (player=='x'):
                                message = 'X Wins!'
                            else:
                                message = 'O Wins!'
                            C.create_text(500/2,500/2,text=message,font=('Purisa',32))
                            C.bind("<Button-1>",new_human_game)
                            
                        # cats game
                        elif (game_state == 'tie'):
                            C.create_rectangle(100,100,500-100,500-100, fill="white")
                            C.create_text(500/2,500/2,text='Tie Game!',font=('Purisa',
                                                                             32))
                            C.bind("<Button-1>",new_human_game)
                            
                        else:
                            # change player
                            player = init.opponent(player)
                        
        C.bind("<Button-1>", move)
        C.pack()
        
        W.mainloop()
        
        
    #--------------------------------------------------------------------------
    """
    new_human_game handler function
    """
    
    # function that starts new game involving humans            
    def new_human_game(event):
        C.delete('all')
        global board
        board = init.new()
        global player
        player = init.random_player()
        draw_lines()
        draw(board)
        add_move_listener()
        
    
    #--------------------------------------------------------------------------
    """
    new_comp_only_game  function
    """
    """
    # function that starts new game involving humans            
    def new_comp_only_game(event):
        C.delete('all')
        global board
        board = init.new()
        global player
        player = init.random_player()
        draw_lines()
        draw(board)
        
        while (init.eval((board,player))):
            # get the next move from the computer
            next_move = comp.chooseMove((board,player),
                                   T.qtable(),T.rtable())
            #implement the next move
            board = init.next_state((board,player),next_move)[0]
            draw(board)
            # change player
            player = init.opponent(player)
        
        game_state = init.eval((board,player))
        
        # somebody won
        if (game_state == 'win'):
            C.create_rectangle(100,100,500-100,500-100, fill="white")
            if (player=='x'):
                message = 'X Wins!'
            else:
                message = 'O Wins!'
            C.create_text(500/2,500/2,text=message,font=('Purisa',32))
            C.bind("<Button-1>",new_game)
            
        # cats game
        if (game_state == 'tie'):
            C.create_rectangle(100,100,500-100,500-100, fill="white")
            C.create_text(500/2,500/2,text='Tie Game!',font=('Purisa',32))
    """

    #--------------------------------------------------------------------------
    """
    play a new game
    """
    
    if (game_type == 'hvh' or game_type == 'hvc'):
        new_human_game('first')
    """
    else:
        new_comp_only_game()
    """
    
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
title = Label(master = W, text = 'Tic Tac Toe', font = ('Cambria', 64*sh/900, 'bold'))
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
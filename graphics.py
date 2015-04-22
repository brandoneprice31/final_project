"""
CS 51

Tic Tac Toe Program

by Vincent Lan, Stephen Albro, Peter Hickman, & Brandon Price
"""


#-----------------------------------------------------------------------------
"""
import modules
"""

from Tkinter import *
import initializer as init


#-----------------------------------------------------------------------------
"""
def start_game function which plays a game given a game_type
"""

def start_game (game_type):
    #--------------------------------------------------------------------------
    """
    initialize board, player, and Canvas
    """
    
    player = init.first_player()
    
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
                    C.bind("<Button-1>",new_game)
                    
                # Cats game
                if (game_state == 'tie'):
                    C.create_rectangle(100,100,500-100,500-100, fill="white")
                    C.create_text(500/2,500/2,text='Tie Game!',font=('Purisa',
                                                                     32))
                    C.bind("<Button-1>",new_game)
                
                # game continues
                else:   
                    # switch player
                    player = init.opponent(player)
                    
                    # if its a hum vs comp game_type
                    if (game_type == 'hvc'):
                        
        
        C.bind("<Button-1>", move)
        C.pack()
        
        W.mainloop()
        
        
    #--------------------------------------------------------------------------
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
        add_move_listener()
    
    
    #--------------------------------------------------------------------------
    """
    play a new the game
    """
    new_game('first')
    
    
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
                 pady = 10, font = ('Purisa', 32))
humvcomp = Button(master = W, text = 'Human vs. Computer', command = hvc, 
                  pady = 10, font = ('Purisa', 32))
compvcomp = Button(master = W, text = 'Computer vs. Computer', command = cvc,
                   pady = 10, font = ('Purisa', 32))

# create title and credits
title = Label(master = W, text = 'Tic Tac Toe', font = ('Cambria', 64, 'bold'))
credits = Label(master = W,
                text = 'by Vincent Lan, Stephen Albro, Peter Hickman, & Brandon Price',
                font = ('Cambria', 12))

# display buttons, title, and credits
title.pack(pady=30)
humvhum.pack(fill=X, pady=20)
humvcomp.pack(fill=X, pady=20)
compvcomp.pack(fill=X, pady=20)
credits.pack(pady=10)

W.mainloop()
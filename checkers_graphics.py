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
import checkers_initializer as init
from random import randint
import checkers_Learning as comp


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
    C = Canvas(W, width=w, height=h)
    
    
    #--------------------------------------------------------------------------
    """
    define comp_ticker which ticks a foo event every second
    """
    
    def comp_tick ():
        global playing
        W.event_generate("<<foo>>")
        if (playing and game_type == 'cvc'):
            W.after(1,comp_tick)
    
    
    #--------------------------------------------------------------------------
    """
    define draw_lines function which draws the lines onto the board
    """
    
    def draw_squares():
        for i in range(8):
            for j in range(8):
                if ((i+j)%2 == 0):
                    C.create_rectangle(i*w/8, j*h/8, (i+1)*w/8, (j+1)*h/8,
                                       fill="black")
                else:
                    C.create_rectangle(i*w/8, j*h/8, (i+1)*w/8, (j+1)*h/8,
                                       fill="white")  
    
    
    #--------------------------------------------------------------------------
    """
    define draw function which draws the current board
    """
    
    def draw(board):
        global state
        board = state['board']
        C.delete('board')
        
        for i in range(8):
            for j in range(8):
                if (board[i][j] == 'rm'):
                    C.create_oval(j*w/8+5,i*h/8+5,(j+1)*w/8-5,(i+1)*h/8-5,
                                  fill='red',tags='board')
                elif (board[i][j] == 'wm'):
                    C.create_oval(j*w/8+5,i*h/8+5,(j+1)*w/8-5,(i+1)*h/8-5,
                                  fill='white',tags='board')
                elif (board[i][j] == 'rk'):
                    C.create_oval(j*w/8+5,i*h/8+5,(j+1)*w/8-5,(i+1)*h/8-5,
                                  fill='red',tags='board')
                    C.create_text(j*w/8+w/16,i*h/8+h/16,text='K',
                                  font=('Purisa',32),fill='black',tags='board')
                elif (board[i][j] == 'wk'):
                    C.create_oval(j*w/8+5,i*h/8+5,(j+1)*w/8-5,(i+1)*h/8-5,
                                  fill='white',tags='board')
                    C.create_text(j*w/8+w/16,i*h/8+h/16,text='K',
                                  font=('Purisa',32),fill='black',tags='board')
                    
           
   #--------------------------------------------------------------------------
    """
    define end game function which draws the end screen
    """
    
    def end_game (game_type, end_type, player):
        # draw white rectangle
        C.create_rectangle(w/8,h/8,w-w/8,h-h/8, fill="white")
        if (end_type == 'r_wins'):
            message = 'Red Wins!'
        else:
            message = 'White Wins!'
        
        C.create_text(w/2,h/2,text=message,font=('Purisa',64))
        if (game_type == 'hvh'):
            C.unbind("<Button-1>")
            W.bind("<Button-1>",new_hvh_game)
        elif (game_type == 'hvc'):
            C.unbind("<Button-1>")
            W.bind("<Button-1>",new_hvc_game)
        elif (game_type == 'cvc'):
            C.unbind("<Button-1>")
            W.bind("<Button-1>",new_cvc_game)
    
    
    #--------------------------------------------------------------------------
    """
    define human_move function which peforms a human move
    """
    def human_move (event):
        # pinpoint which section was clicked
        if (0 <= event.y < h/8):
            new_i = 0
        elif (h/8 <= event.y < 2*h/8):
            new_i = 1
        elif (2*h/8 <= event.y < 3*h/8):
            new_i = 2
        elif (3*h/8 <= event.y < 4*h/8):
            new_i = 3
        elif (4*h/8 <= event.y < 5*h/8):
            new_i = 4
        elif (5*h/8 <= event.y < 6*h/8):
            new_i = 5
        elif (6*h/8 <= event.y < 7*h/8):
            new_i = 6
        else:
            new_i = 7
        if (0 <= event.x < h/8):
            new_j = 0
        elif (h/8 <= event.x < 2*h/8):
            new_j = 1
        elif (2*h/8 <= event.x < 3*h/8):
            new_j = 2
        elif (3*h/8 <= event.x < 4*h/8):
            new_j = 3
        elif (4*h/8 <= event.x < 5*h/8):
            new_j = 4
        elif (5*h/8 <= event.x < 6*h/8):
            new_j = 5
        elif (6*h/8 <= event.x < 7*h/8):
            new_j = 6
        else:
            new_j = 7
        
        # check if this is a valid move
        global state
        global initial_selection
        act = {'init_pos':initial_selection,
               'final_pos':(new_i,new_j)}
        if (init.valid(state['board'],act)):
            # get rid of temporary circles
            C.delete('temp')
            # perform the move
            state = init.next_state(state,act)
            # draw new board
            draw(state['board'])
            
            # check game state
            global player
            game_state = init.eval(state['statr'],state['statw'])
            # if game is over
            if (game_state != 'continue'):
                global playing
                playing = False
                end_game(game_type,game_state,player)
            # game is not over
            else:
                player = init.opponent(player)
                W.after(750, comp_tick)
            
            # bind next selection
            C.bind("<Button-1>", human_selection)
            
            
    #--------------------------------------------------------------------------
    """
    def human_selection which performs a human move
    """
    def human_selection(event):
        
        # pinpoint which section was clicked
        if (0 <= event.y < h/8):
            i = 0
        elif (h/8 <= event.y < 2*h/8):
            i = 1
        elif (2*h/8 <= event.y < 3*h/8):
            i = 2
        elif (3*h/8 <= event.y < 4*h/8):
            i = 3
        elif (4*h/8 <= event.y < 5*h/8):
            i = 4
        elif (5*h/8 <= event.y < 6*h/8):
            i = 5
        elif (6*h/8 <= event.y < 7*h/8):
            i = 6
        else:
            i = 7
        if (0 <= event.x < h/8):
            j = 0
        elif (h/8 <= event.x < 2*h/8):
            j = 1
        elif (2*h/8 <= event.x < 3*h/8):
            j = 2
        elif (3*h/8 <= event.x < 4*h/8):
            j = 3
        elif (4*h/8 <= event.x < 5*h/8):
            j = 4
        elif (5*h/8 <= event.x < 6*h/8):
            j = 5
        elif (6*h/8 <= event.x < 7*h/8):
            j = 6
        else:
            j = 7
        
        global initial_selection
        initial_selection = (i,j)
        
        # check if there this is one of the player's pieces   
        global state
        global player
        if(state['board'][i][j] == player+'m' or
           state['board'][i][j] == player+'k'):
        
            # gather possible moves
            global pos_actions
            pos_actions = init.pos_actions(state['board'],(i,j))
            
            if (pos_actions != []):                    
                # temporarily draw possible actions
                for n in pos_actions:
                    n_i = n['final_pos'][0]
                    n_j = n['final_pos'][1]
                    C.create_oval(n_j*w/8+5,n_i*h/8+5,(n_j+1)*w/8-5,
                                  (n_i+1)*h/8-5,fill='yellow',tags='temp')                  
                C.bind("<Button-1>", human_move)
            # go to the next player if there are no moves left
            if (not init.pos_actions_left(state['board'],player)):
                player = init.opponent(player)
    
    
    #--------------------------------------------------------------------------
    """
    def comp_move which does a computer move
    """
    def comp_move(event):

        global state
        global player        
        
        # get the next move from the computer
        next_move = comp.chooseMove(state['board'],player)
        
        if (next_move == 'nothing'):
            player = init.opponent(player)
        else:
            #implement the next move
            state = init.next_state(state,next_move)
            draw(state['board'])
            
            # check game states
            game_state = init.eval(state['statr'],state['statw'])
            
            # if game is over
            if (game_state != 'continue'):
                global playing
                playing = False
                end_game(game_type,game_state,player)
            # game is not over
            else:
                player = init.opponent(player)

    #--------------------------------------------------------------------------
    """
    new_hvh_game handler function
    """
    
    # function that starts new game involving humans            
    def new_hvh_game(event):
        W.unbind("<Button-1>")
        C.delete('all')
        C.unbind("<Button-1>")
        global state
        state = init.new_game()
        global player
        global playing
        playing = True
        player = init.random_player()
        draw_squares()
        draw(state['board'])
        C.bind("<Button-1>", human_selection)
        C.pack()
        W.mainloop()
        
        
    #--------------------------------------------------------------------------
    """
    new_human_game handler function
    """
    
    # function that starts new game involving human and computer          
    def new_hvc_game(event):
        W.unbind("<Button-1>")
        C.delete('all')
        C.unbind("<Button-1>")
        global state
        state = init.new_game()
        global player
        player = init.random_player()
        draw_squares()
        draw(state['board'])
        global playing
        playing = True
        
        def human_move_bind ():
            C.bind("<Button-1>", human_selection)
        
        W.bind("<<foo>>", comp_move)

        # randomly decide who goes first
        if (randint(0,1) == 0):
            W.after(200, comp_tick)
        
        W.after(300, human_move_bind)
        
        C.pack()
        W.mainloop()
        
        
    #--------------------------------------------------------------------------
    """
    new_cvc_game  function
    """
    
    # function that starts new game involving computers          
    def new_cvc_game(event):
        C.delete('all')
        C.unbind("<Button-1>")
        global state
        state = init.new_game()
        global player
        player = init.random_player()
        draw_squares()
        draw(state['board'])
        global playing
        playing = True
        
        W.bind("<<foo>>",comp_move)
        
        W.after(200,comp_tick)      
        
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

sw = W.winfo_screenwidth()
sh = W.winfo_screenheight()

w = sh - 0.15*sh
h = w

window_x = sw/2 - w/2
window_y = sh/2 - h/2

W.title('Checkers')
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
title = Label(master = W, text = 'Checkers',
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
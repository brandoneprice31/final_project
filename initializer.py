"""
CS 51

Tic Tac Toe Program

by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
"""

from random import randint
from copy import deepcopy

########## TYPES ##############
# type player = X | O

# type action = (int,int)

# type board = array of arrays

# type state = (board*player)

########## FUNCTIONS ############
#-----------------------------------------------------------------------------
"""
new returns an empty board
"""
def new():
    return [['_','_','_'],['_','_','_'],['_','_','_']]

#-----------------------------------------------------------------------------
"""
opponent takes in the current player and returns the next player
"""
def opponent (player):
    if (player == 'x'):
        return 'o'
    else:
        return 'x'

#-----------------------------------------------------------------------------
"""
next_state takes in a board and an action and returns the next state
"""
def next_state(state,action):
    state_copy = deepcopy(state)
    board = state_copy[0]
    player = state_copy[1]
    i = action[0]
    j = action[1]
    board[i][j] = player
    opp = opponent(player)
    nextState = board, opp     
    return nextState
    

#-----------------------------------------------------------------------------
"""
checks if player has won in the state
"""
def win (board, pl):
    if (
    board[0][0] == board[0][1] == board[0][2] == pl or #across the top
    board[1][0] == board[1][1] == board[1][2] == pl or #across the middle
    board[2][0] == board[2][1] == board[2][2] == pl or #across the bottom
    board[0][0] == board[1][0] == board[2][0] == pl or #down the left
    board[0][1] == board[1][1] == board[2][1] == pl or #down the middle
    board[0][2] == board[1][2] == board[2][2] == pl or #down the right
    board[0][0] == board[1][1] == board[2][2] == pl or #top left diagonal
    board[2][0] == board[1][1] == board[0][2] == pl):  #bottom left diagonal
        return True
    else:
        return False

#-----------------------------------------------------------------------------
"""
eval checks if a player won, tied, or continues on a current boards
"""
def eval (state):
    board = state[0]
    
    # check all possible winning cases
    if (win(board,'x')):
        return 'x_win'
    elif (win(board,'o')):
        return 'o_win'
    else: 
        # check if there is '_' which corresponds to continue
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    return 'continue'
                    
        # return tie for cats game
        return 'tie'


#-----------------------------------------------------------------------------
"""
valid takes in a board and action and checks if it is a valid action
"""
def valid (board,action):
    i = action[0]
    j = action[1]
    return (board[i][j] == '_')


#-----------------------------------------------------------------------------
"""
first_player returns the automatic first player of every game
"""
def random_player ():
    if (randint(0,1) == 0):
        return 'x'
    else:
        return 'o'
   
#-----------------------------------------------------------------------------     
"""
returns an empty board and a random player
"""
def new_game ():
  return (new(), random_player())
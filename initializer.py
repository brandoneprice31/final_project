# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:38:26 2015

@author: Stephen
"""

########## TYPES ##############
# type player = X | O

# type action = int (between 1 and 9 inclusive)

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
next_state takes in a state and an action and returns the next state
"""
def next_state(state,action,player):
    i = action[0]
    j = action[1]
    state[i][j] = player
    return state
    

#-----------------------------------------------------------------------------
"""
eval checks if a player won, tied, or continues on a current states
"""
def eval (state,pl):
    # check all possible winning cases
    if (
    state[0][0] == state[0][1] == state[0][2] == pl or #across the top
    state[1][0] == state[1][1] == state[1][2] == pl or #across the middle
    state[2][0] == state[2][1] == state[2][2] == pl or #across the bottom
    state[0][0] == state[1][0] == state[2][0] == pl or #down the left
    state[0][1] == state[1][1] == state[2][1] == pl or #down the middle
    state[0][2] == state[1][2] == state[2][2] == pl or #down the right
    state[0][0] == state[1][1] == state[2][2] == pl or #top left diagonal
    state[2][0] == state[1][1] == state[0][2] == pl):  #bottom left diagonal
        return 'win'
    
    else: 
        # check if there is '_' which corresponds to continue
        for i in range(3):
            for j in range(3):
                if (state[i][j] == '_'):
                    return 'continue'
                    
        # return tie for cats game
        return 'tie'


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
valid takes in a state and action and checks if it is a valid action
"""
def valid (state,action):
    i = action[0]
    j = action[1]
    return (state[i][j] == '_')

#-----------------------------------------------------------------------------
"""
first_player returns the automatic first player of every game
"""
def first_player ():
    return 'x'
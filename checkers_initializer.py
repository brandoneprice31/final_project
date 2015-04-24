"""
CS 51

Tic Tac Toe Program

by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
"""

from random import randint
from copy import deepcopy

########## TYPES ##############
# type player = 'w' | 'r'

# men = 'wm' | 'rm'

# king = 'wk' | 'rk'

# player_type = men | king

# type stats = dict(player:player, men_num:int, king_num:int)

# type action = dict(player_type:player_type, init_pos:(int,int), final_pos:(int,int))

# type board = 8 x 8 array of arrays

# type state = dict(board:board, stats:stats)

########## FUNCTIONS ############
#-----------------------------------------------------------------------------
"""
new returns an empty board
"""
def new():
    return [['wm','_','wm','_','wm','_','wm','_'],\
            ['_','wm','_','wm','_','wm','_','wm'],\
            ['_','_','_','_','_','_','_','_'],\
            ['_','_','_','_','_','_','_','_'],\
            ['_','_','_','_','_','_','_','_'],\
            ['_','_','_','_','_','_','_','_'],\
            ['rm','_','rm','_','rm','_','rm','_'],\
            ['_','rm','_','rm','_','rm','_','rm']]

#-----------------------------------------------------------------------------
"""
opponent takes in the current player and returns the next player
"""
def opponent (player):
    if (player == 'r'):
        return 'w'
    else:
        return 'r'

#-----------------------------------------------------------------------------
"""
next_state takes in a board and an action and returns the next state
"""
def next_state(state,action):
    board = state.board
    stats = state.stats
    player_type = action.player_type
    init_i = action.init_pos[0]
    init_j = action.init_pos[1]
    final_i = action.final_pos[0]
    final_j = action.final_pos[1]
    # add the new move
    if (player_type == 'rm' and final_i == 0):
        board[final_i][final_j] = 'rk'
        stats.king_num += 1
    elif (player_type == 'wm' and final_i == 7):
        board[final_i][final_j] = 'wk'
        stats.king_num += 1
    else:
        board[final_i][final_j] = player_type
    # add the blank space
    board[init_i][init_j] = '_'
    nextState = {'board':board,'stats':stats}
    return nextState
    

#-----------------------------------------------------------------------------
"""
checks if a player has won and returns true or false
"""
def win (stats,opponent_stats):
    if (opponent_stats.men_num == 0 and opponent_stats.king_num == 0):
        return stats.player
    elif (stats.men_num == 0 and stats.king_num == 0):
        return opponent_stats.player
    else:
        return 'none'

#-----------------------------------------------------------------------------
"""
eval checks if either player has won or should continues
"""
def eval (stats1,stats2):
    winning_player = win(stats1,stats2)
    # check all possible winning cases
    if (winning_player == stats1.player):
        return stats1.player + '_wins' # returns either 'w_wins' or 'r_wins'
    elif (winning_player == stats2.player):
        return stats2.player + '_wins' # returns either 'w_wins' or 'r_wins'
    else: 
        return 'continue'


#-----------------------------------------------------------------------------
"""
valid takes in a board and action and checks if it is a valid action
"""
def valid (board,action):
    init_i = action.init_pos[0]
    init_j = action.init_pos[1]
    final_i = action.final_pos[0]
    final_j = action.final_pos[1]
    change_i = final_i - init_i
    change_j = final_j - init_j
    player = action.player_type[0]
    opponent_player = opponent(player)
    
    # check if the action is an open space
    space_is_open = (board[final_i][final_j] == '_')
    
    #check if it is the correct pos for a jump
    if (abs(change_i) == 2 and abs(change_j) == 2):
        correct_pos = (board[init_i + change_i/2][init_j + change_i/2] \
                        == (opponent_player + 'm') or \
                        board[init_i + change_i/2][init_j + change_i/2] \
                        == (opponent_player + 'k'))
        
    #checks if it is the correct pos for a non-jump
    else:
        correct_pos =  (abs(change_i) == 1 and abs(change_j) == 1)
    
    # is it up for red-men
    if (action.player_type == 'rm'):
        correct_direction = (change_i > 0)
        
    # is it down for white-mean
    elif (action.player_type == 'wm'):
        correct_direction = (change_i < 0)
        
    # direction doesn't matter for kings
    else:
        correct_direction = True
        
    # return all three variables
    return (space_is_open and correct_pos and correct_direction)
    
    # Cases:
        # open space - check
        # correct pos for jump - check
        # correct pos for non-jump  - check
        # up for red-men - check
        # down for white-men - check


#-----------------------------------------------------------------------------
"""
pos_actions takes in a board, player_type, and the current_pos of that
player_type.  pos_actions then returns a list of all possible actions
"""
def pos_actions (board, player_type, current_pos):
    return []


#-----------------------------------------------------------------------------
"""
random_player returns a random player
"""
def random_player ():
    if (randint(0,1) == 0):
        return 'w'
    else:
        return 'r'
   
#-----------------------------------------------------------------------------     
"""
returns an empty board and a random player
"""
def new_game ():
  return (new(), random_player())
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 06:59:33 2015

@author: Peter
"""


# type player = 'w' | 'r'

# men = 'wm' | 'rm'

# king = 'wk' | 'rk'

# player_type = men | king

# type stats = dict(player:player, men_num:int, king_num:int)

# type action = dict(init_pos:(int,int), final_pos:(int,int))

# type board = 8 x 8 array of arrays

# type state = dict(board:board, statr:stats, statw:stats)

########## FUNCTIONS ############


import checkers_initializer as I
import checkers_tables as T
import checkers_Learning as L
import pickle

global maxGames
# MaximumGames = 10000000
MaximumGames = 1000

#-----------------------------------------------------------------------------
"""
Plays games to learn q values and returns qTable
"""

def gameLearning(maxGames):
    state = I.new_state()
    games = 0

    # Open the checkers pickled dictionary
    with open('checkers_dict.pickle', 'rb') as handle:
        table = pickle.load(handle)
  
    while (games < maxGames):
        stateKey = T.makeKey(state)
        # print state['player']
        # print state['board']
        if stateKey not in table.keys():
            table = T.addKey(stateKey, table)
        action = L.chooseMove(state,table, games, maxGames)            
        nextState = I.next_state(state,action)
        reward = L.reinforcement(nextState)
        table = L.updateQvalue(state, nextState, reward, table)
        if (I.eval(nextState) == 'continue'):
            state = nextState
        else:
            state = I.new_state()
            games += 1
            print games

    # Save file to checkers pickle
    with open('checkers_dict.pickle', 'wb') as handle:
        pickle.dump(table, handle)
        handle.close()
   
   
gameLearning(100)

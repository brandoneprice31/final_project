# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 07:01:19 2015

@author: Peter
"""

import random
import checkers_initializer as I

qTable = {} # qTable is mutable dict, initialize as dummy stateTable
	# floats [keys in inner actTable] are q-values; we'll update this
	# output a stateTable


# lookup value: stateKey -> action -> table -> value)
# value can be a q-value or a reward
def lookup_value (stateKey, action, stateTable):
    actTable = stateTable[stateKey] 
    return actTable[action]


def makeKey(state): 
    string = ""
    
    # lines below added for testing
    pl = state['player']
    
    for i in range(8):
        for j in range(8):
            string = string + state['board'][i][j]
    string = string + pl
    return string
        
	# take in state and create string representation
	# this key is passed into a statetable, say q table
      # The first 9 characters will be the board, the last  characters will be the player    
        
# Adds the key to qTable, with its value being a dictionary of actions:Qvals
def addKey (state, key, table) : 
    # player
    p = state['player']
    # find all of p's checkers
    list = []
    for i in range(8):
        for j in range(8):
            piece = state['board'][i][j]
            if (piece[0] == p):
                list.append((i,j))
    # loop over p's checkers to find possible actions
    actions = []
    for pos in list:   
        moves = I.pos_actions(state['board'],(pos[0],pos[1]))
        for move in moves:
            actions.append(move)
    print actions
    # Store these action as keys in act_dict, values intially randomized on [-0.15,0.15].
    act_dict = {action:[random.uniform(-0.15,.15), 0] for action in actions}
    # Finally, add the key to the q table, its value being the entire act_dict.
    table[key] = act_dict
    return table
         


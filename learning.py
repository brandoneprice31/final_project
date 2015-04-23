"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

import random as R
import initializer as I
import tables as T

gamma = 0.8 # discount factor
 
#-----------------------------------------------------------------------------
"""
evaluates a board, returning 1 if X won and (-1) if O won, 0 otherwise.
"""

def reinforcement(state):
    if (state[1] == 'x'):
        if (I.eval(state) == 'win'):
            return 1
        elif (I.eval((state[0], 'o')) == 'win'):
            return -1
        else:
            return 0
    if (state[1] == 'o'):
        if (I.eval(state) == 'win'):
            return -1
        elif (I.eval((state[0],'x')) == 'win'):
            return 1
        else:
            return 0

#-----------------------------------------------------------------------------
"""
chooses a move from a given state.
the current algorithm moves randomly half the time and exploit the best q value
the other half

More complicated version to try:
1) Modified Roulette Wheel Selection
2) Code from Mitchell (379)

""" 
  
def chooseMove(state, qTable):
    rand = R.random()
    stateKey = T.makeKey(state)   
    actions = T.getActions(stateKey)
    if rand < 0.5:
        
        # random action
        size = len(actions)
        return actions[R.randint(0,(size-1))]
        
    else:
        # exploit best q-value
        act_dict = qTable[stateKey]
        
        # for player O, reverse sign of q-values in act_dict
        if (state[1] == 'o'):
            for key, value in act_dict.iteritems():
                act_dict[key] = (-1) * value 
                
        # find best move        
        max = -2. # dummy starter value
        for key, value in act_dict.iteritems():
            if value > max:
                best_move = key
        return best_move

#-----------------------------------------------------------------------------
"""
updates q-values in table
"""
def updateQvalue (stateKey, action, nextKey, reward, qTable):
    return ""

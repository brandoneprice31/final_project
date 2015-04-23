"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

import random as R
import initializer as I
import tables as T

all_actions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def reinforcement(board):
    return ""
 
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
              

"""
   
gamma = 0.8 # discount factor
  # We could also assign probabilities for actions using the formula on page 379
  # of the Mitchell book
   
# discount factor 
gamma = 0.8 

def updateQvalue (stateKey, action, nextKey, reward, qTable):
    return ""

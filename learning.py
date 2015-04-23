"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

import random as R
import initializer as I
import tables as T

discountFactor = 0.8
learningRate = 0.5
 
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
finds lowest or highest q-value and returns the move and its q-value
"""

def extremeQvalue(key, player, qTable): 
    actTable = qTable[key]
    if player == 'x': 
        max = -2 # dummy starter value
        for key, value in actTable.iteritems():
            if value > max:
                max = value
                best_action = key
        return best_action, max  
    else:
        min = 2 # dummy starter value
        for key, value in actTable.iteritems():
            if value < min:
                min = value
                best_action = key
        return best_action, min

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
        return extremeQvalue(stateKey, state[1], qTable)[0]

#-----------------------------------------------------------------------------
"""
updates q-values in table
"""

def updateQvalue(stateKey, action, nextKey, reward, qTable):
  if (I.eval == 'win' or I.eval == 'tie'):
     expected = reward
  else:
     # expect opponent to choose next move to optimize against the current player
     player = stateKey[9] 
     expected = reward + (discountFactor * extremeQvalue(nextKey, I.opponent(player), qTable))
  change = learningRate * (expected - qTable[stateKey][action])
  qTable[stateKey][action] += change


  

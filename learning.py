"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

import random as R
import initializer as I
import taaables as T

discountFactor = 0.8
learningRate = 0.8
chooseRandomMove = 0.5
 
#-----------------------------------------------------------------------------
"""
evaluates a board, returning 1 if X won and (-1) if O won, 0 otherwise.
"""
            
def reinforcement(state):
    if I.eval(state) == 'x_win':
            return 1
    elif I.eval(state) == 'o_win':
            return -1
    else:
        return 0

#-----------------------------------------------------------------------------
"""
finds lowest or highest q-value and returns the move and its q-value
"""

def extremeQvalue(key, player, qTable): 
    actTable = qTable[key]
    if player == 'x': 
        maximum = -2 # dummy starter value...whole point is that everything greater than -2
        for key, value in actTable.iteritems():
            if value > maximum:
                maximum = value
                best_action = key
        return (best_action, maximum)  
    else:
        minimum = 2 # dummy starter value
        for key, value in actTable.iteritems():
            if value < minimum:
                minimum = value
                best_action = key
        return (best_action, minimum)

#-----------------------------------------------------------------------------
"""
chooses a move from a given state.
the current algorithm moves randomly half the time and exploit the best q value
the other half

More complicated version to try:
1) Modified Roulette Wheel Selection
2) Code from Mitchell (379)

""" 
  
def chooseMove(state, qTable, games, maxGames):
    stateKey = T.makeKey(state)   
    
    # exploring phase
    if (games < (maxGames * (3/4))):
        rand = R.random()
        actions = T.getActions(stateKey)
        if rand < chooseRandomMove:
            
            # random action
            size = len(actions)
            return actions[R.randint(0,(size-1))]
            
        else:
            # exploit best q-value
            return extremeQvalue(stateKey, state[1], qTable)[0]
            
    # exploitive phase
    else:
        # exploit best q-value
        return extremeQvalue(stateKey, state[1], qTable)[0]

#-----------------------------------------------------------------------------
"""
updates q-values in table
"""


#def updateQvalue(stateKey, action, nextKey, reward, qTable):
#  if (I.eval == 'win' or I.eval == 'tie'):
#     expected = reward
#  else:
#     # expect opponent to choose next move to optimize against the current player
#     player = stateKey[9] 
#     opponent = I.opponent(player)
#     opponent_best = extremeQvalue(nextKey, opponent, qTable)
#     expected = reward + (discountFactor * opponent_best[1])
#  change = learningRate * (expected - qTable[stateKey][action])
#  qTable[stateKey][action] += change


def updateQvalue(firstState, action, nextState, reward, qTable):
    stateKey = T.makeKey(firstState)
    
    # expect opponent to choose next move to optimize against the current player
    if (I.eval(nextState) == 'continue'): 
        nextKey = T.makeKey(nextState)
        player = stateKey[9]    
        opponent = I.opponent(player)
        opponent_best = extremeQvalue(nextKey, opponent, qTable)
        expected = reward + (discountFactor * opponent_best[1])
        change = learningRate * (expected - qTable[stateKey][action])
        qTable[stateKey][action] += change
        return qTable
        
    # game over, so expected is just the final reward
    else:
        print "GAME OVER:"
        print nextState
        print reward
        expected = reward
        change = learningRate * (expected - qTable[stateKey][action])
        qTable[stateKey][action] += change
        return qTable
        
        


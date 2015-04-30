"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

import random as R
import initializer as I
import tables as T

discountFactor = 0.8
learningRate = 0.8
chooseLeastVisited = 0.5
 
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
            if value[0] > maximum:
                maximum = value[0]
                best_action = key
        return (best_action, maximum)  
    else:
        minimum = 2 # dummy starter value
        for key, value in actTable.iteritems():
            if value[0] < minimum:
                minimum = value[0]
                best_action = key
        return (best_action, minimum)
        
#-----------------------------------------------------------------------------
"""
Returns the least visted action from a list of actions. If there are multiple
least-visited actions, it chooses among them randomly
""" 
  
def leastVisited(stateKey, qTable):
    aTable = qTable[stateKey]
    
    # create list of number of visits to each possible new state
    visitsList = map(list, zip(*aTable.values()))[1]
    minimum = min(visitsList)
    least_visited_actions = [x for x in aTable.keys() if (aTable[x][1] == minimum)]
    
    # random action
    size = len(least_visited_actions)
    return least_visited_actions[R.randint(0,(size-1))]

#-----------------------------------------------------------------------------
"""
Chooses a move from a given state. First the first 95% of the games, it 
exploits the best move available half the time and chooses one of the least-
visited moves the other half of the time. In the last 5% of games, it simply 
exploits the best move.
""" 
  
def chooseMove(state, qTable, games, maxGames):
    stateKey = T.makeKey(state)   
    
    # exploring phase
    if (games < (maxGames * 0.95)):
        rand = R.random()
        if rand < chooseLeastVisited:
            print "explore"
            
            # random among least visited actions
            print qTable[stateKey][leastVisited(stateKey, qTable)]
            return leastVisited(stateKey, qTable)
                 
        else:
            print "exploit"
            # exploit best q-value
            print qTable[stateKey][extremeQvalue(stateKey, state[1], qTable)[0]]
            return extremeQvalue(stateKey, state[1], qTable)[0]
            
    # exploitive phase
    else:
        # exploit best q-value
        print "exploit late"
        return extremeQvalue(stateKey, state[1], qTable)[0]

#-----------------------------------------------------------------------------
"""
updates q-values in table
"""

def updateQvalue(firstState, action, nextState, reward, qTable):
    stateKey = T.makeKey(firstState)
    
    # expect opponent to choose next move to optimize against the current player
    if (I.eval(nextState) == 'continue'): 
        nextKey = T.makeKey(nextState)
        player = stateKey[9]    
        opponent = I.opponent(player)
        opponent_best = extremeQvalue(nextKey, opponent, qTable)
        expected = reward + (discountFactor * opponent_best[1])
        change = learningRate * (expected - qTable[stateKey][action][0])
        qTable[stateKey][action][0] += change
        
        # update counter
        qTable[stateKey][action][1] += 1
        return qTable
        
    # game over, so expected is just the final reward
    else:
        print "GAME OVER:"
        expected = reward
        change = learningRate * (expected - qTable[stateKey][action][0])
        qTable[stateKey][action][0] += change
        
        # update counter
        qTable[stateKey][action][1] += 1
        return qTable

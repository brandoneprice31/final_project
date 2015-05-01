# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:31:55 2015
@author: brandoneprice31
"""

import checkers_initializer as I
import checkers_tables as T
import random as R

discountFactor = 0.8
learningRate = 0.8
chooseLeastVisited = 0.5

#-----------------------------------------------------------------------------
"""
evaluates a state, returning 1 if red won and (-1) if white won, 0 otherwise.
"""

def reinforcement(state):
    if I.eval(state) == 'r_wins':
            return 1
    elif I.eval(state) == 'w_wins':
            return -1
    else:
        return 0
        

#-----------------------------------------------------------------------------        
"""
Finds lowest or highest q-value of all the next states that would be generated
from all possible moves. It returns the move and its q-value.
"""

def extremeQvalue(state, player, qTable):
    actions = I.allPosMoves(state['board'], state['player'])
    if player == 'r': 
        maximum = -2 # dummy starter value, since everything greater than -2
        for action in actions:
            new_state = I.next_state(state, action)
            new_key = T.makeKey(new_state)
            if new_key not in qTable.keys():
                qTable = T.addKey(new_key, qTable)
            if qTable[new_key][0] > maximum:
                maximum = qTable[new_key][0]
                best_action = action
        return (best_action, maximum)  
    else:
        minimum = 2 # dummy starter value
        for action in actions:
            new_state = I.next_state(state, action)
            new_key = T.makeKey(new_state)
            if new_key not in qTable.keys():
                qTable = T.addKey(new_key, qTable)
            if qTable[new_key][0] < minimum:
                minimum = qTable[new_key][0]
                best_action = action
        return (best_action, minimum)
    

#-----------------------------------------------------------------------------
"""
Returns the least visted action from a list of actions. If there are multiple
least-visited actions, it chooses among them randomly
""" 
  
def leastVisited(state, qTable):
    actions = I.allPosMoves(state['board'], state['player'])
    
    # create list of action-visits tuples for each possible new state
    actions_visits_list = []    
    for action in actions:
        new_state = I.next_state(state, action)
        new_key = T.makeKey(new_state)
        if new_key not in qTable.keys():
            qTable = T.addKey(new_key, qTable)
        visits = qTable[new_key][1]
        actions_visits_list.append((action,visits))
    
    # make list of least-visited actions
    visitsList = map(list, zip(*actions_visits_list))[1]
    minimum = min(visitsList)
    actions_visits_list = [x for x in actions_visits_list if (x[1] == minimum)]
    least_visited_actions = map(list, zip(*actions_visits_list))[0]
    
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
    pos_act = I.allPosMoves(state['board'], state['player'])
    
    # if some moves are available
    if pos_act != []:
        
        # exploring phase
        if (games < (maxGames * 1.01)):
            rand = R.random()
            if rand < chooseLeastVisited:
                
                # random among least visited actions
                return leastVisited(state, qTable)
                     
            else:
                # exploit best q-value
                return extremeQvalue(state, state['player'], qTable)[0]
                
        # exploitive phase
        else:
            # exploit best q-value
            return extremeQvalue(state, state['player'], qTable)[0]
        
    # if no moves are available
    else:
        return 'nothing'
        
    
#-----------------------------------------------------------------------------
"""
updates q-values in table
"""

def updateQvalue(firstState, nextState, reward, qTable):
    stateKey = T.makeKey(firstState)
    
    if (I.eval(nextState) == 'continue'):
        player = nextState['player']
        opponent = I.opponent(player)
        opponent_best = extremeQvalue(nextState, opponent, qTable)
        expected = reward + (discountFactor * opponent_best[1])
        change = learningRate * (expected - qTable[stateKey][0])
        qTable[stateKey][0] += change
        
        # update no. times visited
        qTable[stateKey][1] += 1
        return qTable
    else:
        expected = reward
        change = learningRate * (expected - qTable[stateKey][0])
        qTable[stateKey][0] += change
        # update no. times visited
        qTable[stateKey][1] += 1
        return qTable
        


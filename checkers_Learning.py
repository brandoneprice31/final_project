# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:31:55 2015

@author: brandoneprice31
"""

import checkers_initializer as I
import checkers_tables as T
from random import randint

#-----------------------------------------------------------------------------
"""
evaluates a state, returning 1 if red won and (-1) if white won, 0 otherwise.
"""

def reinforcement(state):
    if I.eval(state['statr'], state['statw']) == 'r_wins':
            return 1
    elif I.eval(state['statr'], state['statw']) == 'w_wins':
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
            if qTable[new_key][0] > maximum:
                maximum = qTable[new_key][0]
                best_action = action
        return (best_action, maximum)  
    else:
        minimum = 2 # dummy starter value
        for action in actions:
            new_state = I.next_state(state, action)
            new_key = T.makeKey(new_state)
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
    
    # list of two lists: the first is q-values, the
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

def chooseMove(board,player):
    pos_act = I.allPosMoves(board,player)
    if pos_act != []:
        return pos_act[randint(0,len(pos_act)-1)]
    else:
        return 'nothing'
    
#-----------------------------------------------------------------------------
"""
updates q-values in table
"""

def updateQvalue(firstState, action, nextState, reward, qTable):
    return ""
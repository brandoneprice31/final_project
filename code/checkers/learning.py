'''
CS 51
Checkers Program
by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
'''

"""
Learning.py containts functions that are vital to the learning process. Main.py
calls these functions. Perhaps the key functions to highlight in this file are:

1. "Reinforcement": Provides a reward given a state of the board.
2. "UpdateQvalue": Updates the Q value associated with an action and a state. 
   It takes into account the reward of the next state and the opponent's best 
   response. 
3. "ChooseMove": Chooses a move given a board and a player to move. In the 
   exploring phase, we want to strike balance between choosing moves we've 
   already learned and choosing moves that we haven't "visited" much so far. 
   If we're in exploiting mode (such as when the computer plays a human), 
   we're always choosing our qTable's best move.
"""

import initializer as I
import tables as T
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
Helper function: finds lowest or highest q-value of all the next states that 
would be generated from all possible moves. It returns the move and its q-value.
"""
def extremeQvalue(state, player, qTable):
    actions = I.allPosMoves(state['board'], state['player'])
    if player == 'r': 
        # Dummy starter maximum value. Every qValue by definition is greater than -2.
        maximum = -2
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
        # Dummy starter minimum value. Every qValue by definition is smaller than +2.
        minimum = 2
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
Helper function: Returns the least visted action from a list of actions. If there are multiple
least-visited actions, it chooses among them randomly.
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
Chooses a move from a given state. Half the time it exploits the best available
more and the other half of the time it chooses one of the least-visited moves. 
""" 

def chooseMove(state, qTable, games, maxGames):
    pos_act = I.allPosMoves(state['board'], state['player'])
    
    # if some moves are available
    if pos_act != []:
        
        # exploring phase
        if (games < maxGames):
            rand = R.random()
            if rand < chooseLeastVisited:

                # print "explore"
      
                # random among least visited actions
                return leastVisited(state, qTable)
                     
            else:

                # print "exploit"

                # exploit best q-value
                return extremeQvalue(state, state['player'], qTable)[0]
                
        # exploitive phase
        else:
            # exploit best q-value
            # print "exploit late"

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
        


'''
CS 51
Tic Tac Toe Program
by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
'''

"""
Learning.py containts functions that are vital to the learning process. Main.py calls these
functions. Perhaps the key functions to highlight in this file are:
1. "Reinforcement": Provides a reward given a state of the board.
2. "UpdateQvalue": Updates the Q value associated with an action and a state. It takes into
    account the reward of the next state and the opponent's best response. 
3. "ChooseMove": Chooses a move given a board and a player to move. In the exploring phase,
    we want to strike balance between choosing moves we've already learned and choosing moves
    that we haven't "visited" much so far. If we're in exploiting mode (such as when the
    computer plays a human), we're always choosing our qTable's best move.
"""

import random as R
import initializer as I
import tables as T

discountFactor = 0.8
learningRate = 0.8
chooseLeastVisited = 0.5
 
#-----------------------------------------------------------------------------
'''
Reinforcement: X tries to maximize, and O tries to minimize. Reward accordingly. 
'''
def reinforcement(state):
    if I.eval(state) == 'x_win':
            return 1
    elif I.eval(state) == 'o_win':
            return -1
    else:
        return 0

#-----------------------------------------------------------------------------
"""
# Helper function: If the player is X, give us a tuple of the MAXIMALLY Q-valued action
 and its associated Qvalue. If the player is O, give us a tuple of the MINIMALLY
 Q-valued action and its associated Qvalue. The tuple items will be helpful. 
"""
def extremeQvalue(key, player, qTable): 
    actTable = qTable[key]
    if player == 'x': 
        # Dummy starter maximum value. Every qValue by definition is greater than -2.
        maximum = -2
        for key, value in actTable.iteritems():
            if value[0] > maximum:
                maximum = value[0]
                best_action = key
        return (best_action, maximum)  
    else:
        # Dummy starter minimum value. Every qValue by definition is smaller than +2.
        minimum = 2
        for key, value in actTable.iteritems():
            if value[0] < minimum:
                minimum = value[0]
                best_action = key
        return (best_action, minimum)
        
#-----------------------------------------------------------------------------
"""
Helper function: Returns the least visted action from a list of actions. If there are multiple
least-visited actions, it chooses among them randomly.
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
Chooses a move from a given state (board, player). Depending on whether we're in
exploring mode (which we are for the learning process) or exploiting mode,
we will choose differently.
""" 
  
def chooseMove(state, qTable, games, maxGames):
    stateKey = T.makeKey(state)   
    
    # exploring mode
    # When playing computer, games = 1, maxGames = 0 and this mode is never entered.
    if (games < maxGames):
        rand = R.random()
        if rand < chooseLeastVisited:            
            # Sometimes, choose randomly among least visited actions
            return leastVisited(stateKey, qTable)
                 
        else:
            # Other times, choose the best move we've learned so far.
            return extremeQvalue(stateKey, state[1], qTable)[0]
            
    # exploitive mode
    else:
        # Choose the best move according to the qTable. 
        return extremeQvalue(stateKey, state[1], qTable)[0]

#-----------------------------------------------------------------------------
"""
updateQValue: Do this based on the opponents best response to our already-decided action,
and based on the pure reward associated with the next state. The reward is either -1 (o wins),
+1 (x wins) or 0 (the game is not over yet).
"""

def updateQvalue(firstState, action, nextState, reward, qTable):
    stateKey = T.makeKey(firstState)
    
    # Expect opponent to choose next move to optimize against the current player
    if (I.eval(nextState) == 'continue'): 
        nextKey = T.makeKey(nextState)
        # Get the player and opponent. 
        player = stateKey[9]    
        opponent = I.opponent(player)
        # Get the opponents best move. This is a tuple (best_move, associated qVal).
        opponent_best = extremeQvalue(nextKey, opponent, qTable)
        # Discount your reward (of 0--there for consistency) by your opponents best response. 
        expected = reward + (discountFactor * opponent_best[1])
        
    # Game over, so the reward will not be discounted at all. 
    else:
        expected = reward
        
    # Store the "improvement" on the current qValue in a variable called change. 
    # This depends on our learningRate.  
    change = learningRate * (expected - qTable[stateKey][action][0])
    # Add the improvement to the current qValue.
    qTable[stateKey][action][0] += change
    # Increment the number-of-times-we've-made-this-move counter.
    qTable[stateKey][action][1] += 1
    # Return the table.
    return qTable

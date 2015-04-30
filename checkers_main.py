# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 06:59:33 2015

@author: Peter
"""


# type player = 'w' | 'r'

# men = 'wm' | 'rm'

# king = 'wk' | 'rk'

# player_type = men | king

# type stats = dict(player:player, men_num:int, king_num:int)

# type action = dict(init_pos:(int,int), final_pos:(int,int))

# type board = 8 x 8 array of arrays

# type state = dict(board:board, statr:stats, statw:stats)

########## FUNCTIONS ############


import checkers_initializer as I
import checkers_tables as T
import checkers_learning as L
import pickle

global maxGames
# MaximumGames = 10000000
MaximumGames = 30000

#-----------------------------------------------------------------------------
"""
Plays games to learn q values and returns qTable
"""

def gameLearning(maxGames):
    state = I.new_game()
    games = 0

    # Open the CHECKERS CHECKERS CHECKERS CHECKERS pickled dictionry
    # with open('checkers_dict.pickle', 'rb') as handle:
        # table = pickle.load(handle)
  
    while (games < maxGames):
        stateKey = T.makeKey(state)
        if stateKey not in table.keys():
            table = T.addKey(stateKey, table)
        action = L.chooseMove(state,table, games, maxGames)
        nextState = I.next_state(state,action)
        nextKey = T.makeKey(nextState)
        reward = L.reinforcement(nextState)
        if nextKey not in table.keys():
            table = T.addKey(nextState, nextKey, table)
        table = L.updateQvalue(state, action, nextState, reward, table)
        if (I.eval(nextState) == 'continue'):
            state = nextState
        else:
            for i in range(8):  
                print state['board'][i]
            print "----------"
            print "NEW GAME:"
            state = I.new_game()
            games += 1
    
    tabletoprint = []
    
    """     
    for state,actTable in table.iteritems():
        for action,qValue in actTable.iteritems():
            if (qValue[0] > 0.15 or qValue[0] < -0.15):
                tabletoprint.append((state, action, qValue))
    """
    
    for state,actTable in table.iteritems():
        for action,qValue in actTable.iteritems():
            if (qValue[1] > 400):
                tabletoprint.append((state, action, qValue))
    
    # print table
    # print tabletoprint
    
    # save the table in the pickle file

    # with open('dict.pickle', 'wb') as handle:
      #   pickle.dump(table, handle)

    with open('checkers_dict.pickle', 'wb') as handle:
        pickle.dump(table, handle)
        handle.close()
        
    return table
    
gameLearning(MaximumGames)

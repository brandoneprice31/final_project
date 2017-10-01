'''
CS 51
Checkers Program
by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
'''

'''
Main.py runs the learning process, calling on functions from the learning module.
'''

import initializer as I
import tables as T
import learning as L
import pickle

global maxGames
MaximumGames = 30000

#-----------------------------------------------------------------------------
"""
Plays games to learn q values and "pickles" qTable to a file.
"""

def gameLearning(maxGames):
    state = I.new_state()
    games = 0

    # Open the checkers pickled dictionary
    with open('dict.pickle', 'rb') as handle:
        table = pickle.load(handle)
        
    # Play games
    while (games < maxGames):
        stateKey = T.makeKey(state)
        if stateKey not in table.keys():
            table = T.addKey(stateKey, table)
        # Choose a move from the table.
        action = L.chooseMove(state, table, games, maxGames)            
        # Choose a move from the table.        
        nextState = I.next_state(state,action)
        # Save a "reward" associated with the state resulting from that move.        
        reward = L.reinforcement(nextState)
        # Update the qTable according to the reward.
        table = L.updateQvalue(state, nextState, reward, table)   
        # Keep playing,        
        if (I.eval(nextState) == 'continue'):
            state = nextState
        # or start a new game and learn some more.        
        else:
            state = I.new_state()
            games += 1
            print (games)


    # After maxGames have been played, save the table into the pickle file.
    with open('dict.pickle', 'wb') as handle:
        pickle.dump(table, handle)
        handle.close()


gameLearning(2000)
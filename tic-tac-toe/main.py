'''
CS 51
Tic Tac Toe Program
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
    state = I.new_game()
    games = 0

    # Open the pickled dictionary.
    with open('dict.pickle', 'rb') as handle:
        table = pickle.load(handle)
  
    while (games < maxGames):
        print state[0][0]
        print state[0][1]
        print state[0][2]
        print "-----------"
        stateKey = T.makeKey(state)
        if stateKey not in table.keys():
            table = T.addKey(stateKey,table)
        # Choose a move from the table.
        action = L.chooseMove(state,table, games, maxGames)
        # Get the state resulting from that move.
        nextState = I.next_state(state,action)
        nextKey = T.makeKey(nextState)
        # Save a "reward" associated with the state resulting from that move.
        reward = L.reinforcement(nextState)
        # Add the key of that next state if necessary.
        if nextKey not in table.keys():
            table = T.addKey(nextKey,table)
        # Update the qTable according to the reward.
        table = L.updateQvalue(state, action, nextState, reward, table)
        # Keep playing,
        if (I.eval(nextState) == 'continue'):
            state = nextState
        # or start a new game and learn some more.
        else:
            state = I.new_game()
            games += 1
            print state[0][0]
            print state[0][1]
            print state[0][2]
            print "-----------"
    
    # After maxGames have been played, save the table into the pickle file.
    with open('dict.pickle', 'wb') as handle:
        pickle.dump(table, handle)
        handle.close()
    
    print table        
        
gameLearning(3000)

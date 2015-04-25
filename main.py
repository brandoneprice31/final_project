import initializer as I
import tables as T
import learning as L
import pickle

global maxGames
MaximumGames = 30000

#-----------------------------------------------------------------------------
"""
Plays games to learn q values and returns qTable
"""

def gameLearning(maxGames):
    state = I.new_game()
    games = 0
    execfile("pickle_initializer.py")

    # Open the pickled dictionry
    with open('dict.pickle', 'rb') as handle:
        table = pickle.load(handle)
  
    while (games < maxGames):
        print state[0][0]
        print state[0][1]
        print state[0][2]
        print "----------"
        stateKey = T.makeKey(state)
        if stateKey not in table.keys():
            table = T.addKey(stateKey,table)
        action = L.chooseMove(state,table, games, maxGames)
        nextState = I.next_state(state,action)
        nextKey = T.makeKey(nextState)
        reward = L.reinforcement(nextState)
        if nextKey not in table.keys():
            table = T.addKey(nextKey,table)
        table = L.updateQvalue(state, action, nextState, reward, table)
        if (I.eval(nextState) == 'continue'):
            state = nextState
        else:
            print nextState[0][0]
            print nextState[0][1]
            print nextState[0][2]
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
    with open('dict.pickle', 'wb') as handle:
        pickle.dump(table, handle)
        handle.close()
        
    return table
    
gameLearning(30000)

# pick move that it has explored the least so far

  

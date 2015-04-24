import initializer as I
import tables as T
import learning as L

global maxGames
MaximumGames = 30000

#-----------------------------------------------------------------------------
"""
Plays games to learn q values and returns qTable
"""

def gameLearning(maxGames):
    state = I.new_game()
    games = 0
    table = T.qTable
  
    while (games < maxGames):
        stateKey = T.makeKey(state)
        if stateKey not in table.keys():
            table = T.addKey(stateKey,table)
        action = L.chooseMove(state,table)
        nextState = I.next_state(state,action)
        nextKey = T.makeKey(nextState)
        reward = L.reinforcement(nextState)
        if nextKey not in table.keys():
            table = T.addKey(nextKey,table)
        table = L.updateQvalue(stateKey, action, nextKey, reward, table)
        if (I.eval(nextState) == 'win'):
            state = I.new_game()
            games += 1
        else:
            state = nextState
       
    return table
  

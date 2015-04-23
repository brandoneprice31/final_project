import initializer as I
import tables as T
import learning as L

global maxGames
MaximumGames = 30000

""" 
Plays games to learn q values and returns qTable
"""
def gameLearning(maxGames):

  state = I.new_game
  games = 0
  table = T.qTable
  
  while (games < maxGames):
    stateKey = T.makeKey(state)
    if stateKey not in table.keys(): # I think this is actually correct syntax.
       T.addKey(stateKey,table)
    action = L.chooseMove(state,table)
    nextState = I.next_state(state,action)
    nextKey = T.makeKey(nextState)
    reward = L.reinforcement(nextState[0])
    if nextKey not in table.keys():
       T.addKey(nextKey,table)
    table = L.updateQvalues(stateKey, action, nextKey, reward, table)
    if (I.eval(nextState) == 'win'):
       state = I.new_game
       games += 1
    else:
       state = nextState
       
  return table
      
"""
Uses qTable to compete against a human player
"""
def compete(qtable):




# IGNORE THESE ARE STEPHen's musings

# Pseudocode: What will main.py do?

# blank qTable set and ready to go
# Questions:

# 1. How will the algorithm choose a move if it has never seen this board before?
# 2. 

# initial board with 1 move done given to alg
# alg chooses a move
# alg updates qTable with new board (and ACT TABLE from that board?)
# another move is made and board 
# is handed to alg again (maybe have a while (game not over) loop to keep doing this)
# Alg chooses a move
# alg updates qTable with new board (" ")
# this repeats until the game is over
# When the game is over if alg loses, we somehow need to go back and weigh each choice that alg made
# ^^^how?
# If alg wins, we need to go back and weigh the choices that alg made (how?) How to
# do this 1) syntactically and 2) functionally: how to weigh choices with weights?
# "Tie" ?

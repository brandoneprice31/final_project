import initializer as I
import tables as T
import learning as L

global maxGames
MaximumGames = 30000

## PseudoCODE FROM ONLINE
def gameLearning(maxGames):

  board = I.new()
  player = I.random_player()
  state = (board, player)
  games = 0
  table = T.qTable
  
  while (games < maxGames):
    stateKey = T.makeKey(state)
    if stateKey not in table.keys():
       T.addKey(stateKey)
    action = L.chooseAction(stateKey,table)
    nextBoard = I.next_state(state,action)[1]
    nextKey = T.makeKey(nextState, I.opponent(player))
    reward = L.reinforcement(nextBoard)
    if nextKey not in table.keys()
       addKey(nextKey)
    updateQvalues(stateKey, action, nextKey, reward)
    if game over
       reset game
       board = startBoard
       games += 1
    else
       board = nextBoard
       switchPlayers()



gameLearning(I.new(), MaximumGames)



















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

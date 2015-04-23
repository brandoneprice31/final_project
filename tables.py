import initializer as init
import random

# "type" isn't a thing in python
type stateTable = dict() # dictionary with states as keys and actTables as values

type actTable = dict ()# dictionary with squares as keys and floats as values 

qTable = dict() # qTable is mutable dict, initialize as dummy stateTable
	# floats [keys in inner actTable] are q-values; we'll update this
	# output a stateTable

rewardTable = () # rewardTable is mutable dict, how to initialize?
	# floats [keys in inner actTable] are rewards [0, 1, or -1]; don't update this

def value (board, square, qTable): 
    # WE will probably come across this function when we implement choosemove
    # I'll wait until then to implement it.
    
    
    # ((( float (* looks up q-value for board and next move square*)
    # lookup board in qTable, return the actTable
    # lookup square in actTable, retun q-value )))

def makeKey (state) : 
    string = ""
    board = state[0]
    pl = state[1]
    for i in range(3):
        for j in range(3):
            string = string + state[0][i][j]
    string = string + pl
    return string
        
	# take in state and create string representation
	# this key is passed into a statetable, say q table
      # The first 9 characters will be the board, the last  characters will be the player

def nextKey (state) : 
    makeKey (nextState, opponent(player))
    ## What's up with this function? Not sure we need it.
    ## In main.py, nextKey is a VARIABLE, not a function.

# HELPER FUNCTION: Gets possible actions (ints) from KEYS (string representations of states)
#   Iterate over the string, saving the index (number) of each '_' that appears.
#   (Note that we should never get the number 9 as an action, because actions only range
#   0-8; the ninth charactr in a key always refers to the PLAYER and thus should never be '_'.)
#   This list of indices is your set of actions.
#   This function returns a LIST OF INTEGERS.
def getActions(key):
    action_list = []
    list_form = list(key)
    for i in range(len(list_form)):
        if (list_form[i] == '_'):
            action_list.append(i)
    return action_list
        
        
# Adds the key to qTable, with its value being a dictionary of actions:Qvals
def addKey (key, table) : 
    # Get list of potential actions from the key. This is an int list.
    actions = getActions(key)
    # Store these action as keys in act_dict, values intially randomized on [-0.15,0.15].
    act_dict = {action:random.uniform(-0.15,.15) for action in actions}
    # Finally, add the key to the q table, its value being the entire act_dict.
    table[key] = act_dict
         
    


# import initializer as init

# stateTable and actTables are types
# stateTable: dictionary with states as keys and actTables as values
# actTable: dictionary with actions as keys and floats as values (Q values)

# To instantiate a qTable or rewardTable (this will be done in main.py), 
# do the following:
# qTable = dict()		<-- values in actTable are qvalues

# rewardTable = dict()  <-- values in actTable are rewards
import initializer as init
import random

"""
# "type" isn't a thing in python
type stateTable = dict() # dictionary with states as keys and actTables as values

type actTable = dict ()# dictionary with squares as keys and floats as values 
"""

qTable = {} # qTable is mutable dict, initialize as dummy stateTable
	# floats [keys in inner actTable] are q-values; we'll update this
	# output a stateTable


# lookup value: stateKey -> action -> table -> value)
# value can be a q-value or a reward
def lookup_value (stateKey, action, stateTable):
    actTable = stateTable[stateKey] 
    return actTable[action]


def makeKey(state): 
    string = ""
    
    # lines below added for testing
    pl = state[1]
    
    for i in range(3):
        for j in range(3):
            string = string + state[0][i][j]
    string = string + pl
    return string
        
	# take in state and create string representation
	# this key is passed into a statetable, say q table
      # The first 9 characters will be the board, the last  characters will be the player



"""
def nextKey (state) : 
    makeKey (nextState, opponent(player))
    ## What's up with this function? Not sure we need it.
    ## In main.py, nextKey is a VARIABLE, not a function.
    
    # PETER: I agree, I don't think we need this
"""

# HELPER FUNCTION: Gets possible actions (ints) from KEYS (string representations of states)
#   Iterate over the string, saving the index (number) of each '_' that appears.
#   (Note that we should never get the number 9 as an action, because actions only range
#   0-8; the ninth charactr in a key always refers to the PLAYER and thus should never be '_'.)
#   This list of indices is your set of actions.
#   This function returns a LIST OF INTEGERS.
def getActions(key):
    all_actions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    action_list = []
    list_form = list(key)
    for i in range(len(list_form)):
        if (list_form[i] == '_'):
            action_list.append(all_actions[i])
    return action_list
        
        
# Adds the key to qTable, with its value being a dictionary of actions:Qvals
def addKey (key, table) : 
    # Get list of potential actions from the key. This is an int list.
    actions = getActions(key)
    # Store these action as keys in act_dict, values intially randomized on [-0.15,0.15].
    act_dict = {action:random.uniform(-0.15,.15) for action in actions}
    # Finally, add the key to the q table, its value being the entire act_dict.
    table[key] = act_dict
    return table
         


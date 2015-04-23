import initializer as init

# "type" isn't a thing in python
type stateTable = dict() # dictionary with states as keys and actTables as values

type actTable = dict ()# dictionary with squares as keys and floats as values 

qTable = dict() # qTable is mutable dict, initialize as dummy stateTable
	# floats [keys in inner actTable] are q-values; we'll update this
	# output a stateTable

rewardTable = () # rewardTable is mutable dict, how to initialize?
	# floats [keys in inner actTable] are rewards [0, 1, or -1]; don't update this

def value (board, square, qTable): 
	# float (* looks up q-value for board and next move square*)
    # lookup board in qTable, return the actTable
    # lookup square in actTable, retun q-value

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
def getActions(key):
    # Iterate over the string, saving the index (number) of each '_' that appears.
    # (Note that we should never get the number 9 as an action, because actions only range
    # 0-8; the ninth charactr in a key always refers to the PLAYER and thus should never be '_'.)
    # thislist is your set of actions.
    # This function should return a LIST OF INTEGERS
    action_list = []
    list_form = list(key)
    for i in range(len(list_form)):
        if (list_form[i] == '_'):
            action_list.append(i)
    return action_list
        
        

def addKey (string) : 
    # add row to rewardTable & qTable with this key reward is 0 and q-value is 0 *)
    # add the key to qTable
    # get all the possible actions from the key
    # set the value of the qtable at this key to ANOTHER DICTIONARY, the action dictionary,
    # whose keys are each these actions (actions represented as integers)
    # initialize the values associated with these action keys in the action dict to be
    # random on [-0.15,0.15]
    

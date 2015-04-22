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

def addKey (string) : 
	# add row to rewardTable & qTable with this key reward is 0 and q-value is 0 *)

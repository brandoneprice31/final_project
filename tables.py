# import initializer as init

# stateTable and actTables are types
# stateTable: dictionary with states as keys and actTables as values
# actTable: dictionary with actions as keys and floats as values (Q values)

# To instantiate a qTable or rewardTable (this will be done in main.py), 
# do the following:
# qTable = dict()		<-- values in actTable are qvalues

# rewardTable = dict()  <-- values in actTable are rewards

rewardTable = dict() # rewardTable is mutable dict, how to initialize?
	# floats [keys in inner actTable] are rewards [0, 1, or -1]; don't update this

# lookup value: stateKey -> action -> table -> value)
# value can be a q-value or a reward
def lookup_value (stateKey, action, stateTable):
	actTable = stateTable.get(stateKey)
	value = actTable.get(action)
	return value

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

def addKey (key) : 
	# add row to rewardTable & qTable with this key reward is 0 and q-value is 0 *)


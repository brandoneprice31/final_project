'''
CS 51
Tic Tac Toe Program
by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
'''

'''
Tables.py is our file which contains functions necessary for manipulating data structures.
In this case, we are concerned with manipulating our qTable, which is a dictionary.
The keys are string representations of our states: (board, player).
The values are themselves dictionaries, with the keys being actions (moves) and the
values being a tuple of (Qvalue, number of times we've made the action). 
'''

import random

# Given a state tuple of (board, player), convert this into a string key for Q-table dict.
# Characters 0-8 will represent the board; character 9 the player to move.
def makeKey(state): 
    string = ""
    # Get the board characters.    
    for i in range(3):
        for j in range(3):
            string = string + state[0][i][j]
    # Add the player character.
    pl = state[1]
    string = string + pl
    return string


# Helper function: Gets possible actions (coordinate pairs) from a key (string).
# (Note that we should never get the number 9 as an action, because actions only range
#  0-8; the ninth charactr in a key always refers to the PLAYER and thus should never be '_'.)
#  This function returns a list of tuples.
def getActions(key):
    # Each coordinate pair nicely correlates with the board position of the its index in this list.
    all_actions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    action_list = []
    list_form = list(key)
    # If the board is blank in position i, all_actions[i] is a valid action.
    for i in range(len(list_form)):
        if (list_form[i] == '_'):
            action_list.append(all_actions[i])
    return action_list
        
        
# Adds the key(string) to the qTable. 
def addKey (key, table) : 
    # Get list of potential actions from the key. This is a list of tuples.
    actions = getActions(key)
    # Store these action as keys in act_dict, values intially randomized on [-0.15,0.15].
    act_dict = {action:[random.uniform(-0.15,.15), 0] for action in actions}
    # Finally, add the key to the q table, its value being the entire act_dict.
    table[key] = act_dict
    return table
         


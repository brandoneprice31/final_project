'''
CS 51
Checkers Program
by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
'''

'''
Tables.py is our file which contains functions necessary for manipulating data structures.
In this case, we are concerned with manipulating our qTable, which is a dictionary.
The keys are string representations of our states, which are eight-character
strings that describe the numbers of different types of pieces on the board.
The values are tuples of (Qvalue, number of times we've made the action). 
'''

import random

# Given a state tuple of (board, player), convert this into a string key for 
# Q-table dict. The first two characters are the number of red men, the next 
# two are red kings, then white men, then white kings.
def makeKey(state): 
    rmen = state['statr']['men_num']
    rkings = state['statr']['king_num']
    wmen = state['statw']['men_num']
    wkings = state['statw']['king_num']
    
    # make them into strings, always exactly 2 digits long
    if (rmen >= 10):
        rmenstr = str(rmen)
    else:
        rmenstr = '0' + str(rmen)

    if (rkings >= 10):
        rkingsstr = str(rkings)
    else:
        rkingsstr = '0' + str(rkings)

    if (wmen >= 10):
        wmenstr = str(wmen)
    else:
        wmenstr = '0' + str(wmen)

    if (wkings >= 10):
        wkingsstr = str(wkings)
    else:
        wkingsstr = '0' + str(wkings)
        
    # concatenate
    return (rmenstr + rkingsstr + wmenstr + wkingsstr)
        
# Adds the key(string) to the qTable. 
def addKey (key, table): 
    table[key] = [random.uniform(-0.15,.15),1]
    return table
         


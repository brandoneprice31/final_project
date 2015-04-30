# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 07:01:19 2015

@author: Peter
"""

import random
import checkers_initializer as I

qTable = {} # qTable is mutable dict, initialize as dummy stateTable
	# floats [keys in inner actTable] are q-values; we'll update this
	# output a stateTable

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
        
    return (rmenstr + rkingsstr + wmenstr + wkingsstr)
        

# Adds the key to qTable, with its value being a tuple (initial random Q val, no. times visited)
def addKey (key, table): 
    table[key] = (random.uniform(-0.15,.15),1)
    return table
         


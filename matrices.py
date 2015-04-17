# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:38:41 2015

@author: Stephen
"""

import initializer as init

type stateTable = dict # dictionary with states as keys and actTables as values

type actTable = dict # dictionary with squares as keys and floats as values 

qTable = ??? # qTable is mutable dict, initialize as dummy stateTable
	# floats [keys in inner actTable] are q-values; we'll update this
	# output a stateTable

rewardTable = ??? # rewardTable is mutable dict, how to initialize?
	# floats [keys in inner actTable] are rewards [0, 1, or -1]; don't update this

def value (board, square, qTable): 
	# float (* looks up q-value for board and next move square*)

def makeKey (state) : 
	# take in state and create string representation
	# this key is passed into a statetable, say q table

def nextKey (state) : 
	makeKey (nextState, opponent(player))

def addKey (string) : 
	# add row to rewardTable & qTable with this key reward is 0 and q-value is 0 *)

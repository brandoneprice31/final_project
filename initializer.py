# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:38:26 2015

@author: Stephen
"""

########## TYPES ##############
# type player = X | O

# type action = int (between 1 and 9 inclusive)

# type board = array of arrays

# type state = (board*player)

########## FUNCTIONS ############
# new(unit): state (empty board and player to move first)
# next_state(state,action): state
# eval (state) = player | tie | continue
# opponent (player) = the other player
# valid (state,action): bool (is the move legal)
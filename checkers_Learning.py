# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:31:55 2015

@author: brandoneprice31
"""

import checkers_initializer as I
from random import randint

def reinforcement(state):
    if I.eval(state['statr'], state['statw']) == 'r_wins':
            return 1
    elif I.eval(state['statr'], state['statw']) == 'w_wins':
            return -1
    else:
        return 0

def chooseMove(board,player):
    pos_act = I.allPosMoves(board,player)
    if pos_act != []:
        return pos_act[randint(0,len(pos_act)-1)]
    else:
        return 'nothing'
    

#def reinforcement

#def updateQvalue
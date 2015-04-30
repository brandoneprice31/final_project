# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:31:55 2015

@author: brandoneprice31
"""

import checkers_initializer as init
from random import randint

def chooseMove(board,player):
    pos_act = init.allPosMoves(board,player)
    if pos_act != []:
        return pos_act[randint(0,len(pos_act)-1)]
    else:
        return 'nothing'
    

#def reinforcement

#def updateQvalue
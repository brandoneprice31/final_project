# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:31:55 2015

@author: brandoneprice31
"""

import checkers_initializer as init
from random import randint

def chooseMove(board,player):
    pos_act = []
    for i in range(8):
        for j in range(8):
            if (board[i][j] == player+'m' or board[i][j] == player+'k'):
                for act in init.pos_actions(board,(i,j)):
                    pos_act.append(act)
    if (pos_act == []):
        return 'nothing'
    return pos_act[randint(0,len(pos_act) - 1)]
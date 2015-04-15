# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:17:49 2015

@author: Stephen
"""

#Sample boards for testing:
board1=[[1,2,3][4,5,6],[7,8,9]]

board = [[0 for y in range(3)] for x in range(3)]
#board[1][2] = 5
#board [0][1] = 4
#board [2][0] = 3
def won_white (board):
    won = False
    # Check horizontal wins
    for row in range(3):
        if ((board [row][1] == board[row][2]) and (board[row][0] == board[row][1])):
            won = True
    for col in range(3):
        if ((board [0][col] == board[1][col]) and (board[1][col] == board[2][col])):
            won = True
    print won
    

won_white (board)
            

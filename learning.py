"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

import Matrices as M
import Initializer as I

def chooseMove(stateKey, qTable): 
  actTable = value[stateKey]
  possible_actions = []
  List.filter (fun a -> I.valid) actions
  values = list of values in actTable
  if player is X
     lowest = min(values)
  else
     reverse the sign of each value in values list
     lowest = min(values)
  if lowest < 0
     constant = abs(lowest) + 0.1
     add this constant to each value in values list to make all values positive
  now perform modified roulette wheel selection using k
  
  We could also assign probabilities for actions using the formula on page 379
  of the Mitchell book
   """
   
gamma = 0.8 # discount factor 

def updateQvalue (stateKey, action, nextKey, reward, qTable):
    """"
    udpates the qTable using the function Q*(s,a) <- r + gamma*min_(a’)Q*(s’,a’)
    Returns the float that should replace the q-value in the qTable
    
    Pseduocode:
    
    possible_actions = List.filter (fun a -> I.valid) (qTable[nextKey])
    min_qvalue = find minimum Q value among actions
    reward + gamma * min_qvalue
    """

def reinforcement (board):
    """"
    if the state is a win for x, return 1, if win for o, return -1, otherwise
    initialize to a random number on [-0.15,0.15]. at least this is
    how i understand it now
    """"

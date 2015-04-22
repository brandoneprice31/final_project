"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

from random import randint
import initializer as I

all_actions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def reinforcement(board):
    return ""
    
def chooseMove(state, qTable):
  possible_actions = []
  for i in all_actions:
      if (I.valid(state[0],i)):
          possible_actions.append(i)
  size = len(possible_actions)
  return possible_actions[randint(0,(size-1))]

"""
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
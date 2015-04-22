"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

from random import randint
import Matrices as M
import initializer as I

all_actions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def reinforcement(board):
    return ""
    
def chooseMove_random(state, qTable):
  possible_actions = [i for i in all_actions if I.valid(state[0],i) == True]
  size = len(possible_actions)
  return all_actions[randint(0,(size-1))]


def chooseMove(state, qTable): 
  stateKey = T.makeKey(state)
  actTable = qTable.get(stateKey, default=None)
  possible_actions = [i for i in all_actions if (I.valid(state[0],i) == True)]
  size = len(possible_actions)
  values = actTable.values()
  if (state[1] == 'x'):
     lowest = min(values)
  else:
     values = [i for i in values (-i)]
     lowest = min(values)
  if lowest < 0:
     constant = abs(lowest) + 0.1
     
     # add this constant to each value in values list to make all values positive
     # now perform modified roulette wheel selection using k
  
  # We could also assign probabilities for actions using the formula on page 379
  # of the Mitchell book
   
# discount factor 
gamma = 0.8 

def updateQvalue (stateKey, action, nextKey, reward, qTable):
    """"
    udpates the qTable using the function Q*(s,a) <- r + gamma*min_(a’)Q*(s’,a’)
    Returns the new Q table
    
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

"""
Created on Fri Apr 17 13:39:00 2015

@author: Peter
"""

from random import randint
import initializer as I

all_actions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def reinforcement(state):
    if (state[1] == 'x'):
        if (I.eval(state) == 'win'):
            return 1
        elif (I.eval((state[0], 'o')) == 'win'):
            return -1
        else:
            return 0
    if (state[1] == 'o'):
        if (I.eval(state) == 'win'):
            return -1
        elif (I.eval((state[0],'x')) == 'win'):
            return 1
        else:
            return 0


def chooseMove(state, qTable):
  possible_actions = []
  for i in all_actions:
      if (I.valid(state[0],i)):
          possible_actions.append(i)
  size = len(possible_actions)
  return possible_actions[randint(0,(size-1))]

"""

def chooseMove_random(state, qTable):
  possible_actions = []
  for i in all_actions:
      if I.valid(state,all_actions[i]) == True:
          possible_actions.append(all_actions[i])
  size = len(possible_actions)
  return all_actions[randint(0,(size-1))]

def chooseMove(state, qTable): 
  stateKey = T.makeKey(state)
  actTable = qTable.get(stateKey, default=None)
  possible_actions = [i for i in all_actions if (I.valid(state[0],i) == True)]
  size = len(possible_actions)
  values = actTable.values()
  if (state[1] == 'x'):
>>>>>>> 7448961435cb656b3ad91bf4ce3d26f3d1710c92
     lowest = min(values)
  else:
     values = [i for i in values (-i)]
     lowest = min(values)
  if lowest < 0:
     constant = abs(lowest) + 0.1     
     # add this constant to each value in values list to make all values positive
     # now perform modified roulette wheel selection using k
  
  We could also assign probabilities for actions using the formula on page 379
  of the Mitchell book
"""
   
gamma = 0.8 # discount factor
  # We could also assign probabilities for actions using the formula on page 379
  # of the Mitchell book
   
# discount factor 
gamma = 0.8 

def updateQvalue (stateKey, action, nextKey, reward, qTable):
    return ""

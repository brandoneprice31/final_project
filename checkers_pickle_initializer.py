# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:19:51 2015

@author: Stephen
"""
import pickle

d = {}

# This is how you "Dump" TO the pickle
with open('checkers_dict.pickle', 'wb') as handle:
    pickle.dump(d, handle)

  
## This is how you "load" FROM the pickle
#with open('dict.pickle', 'rb') as handle:
#    b = pickle.load(handle)
#
#print b == d
#
#r = {'h':2}
#with open('dict.pickle','wb') as handle:
#    pickle.dump(r, handle)
#
#with open ('dict.pickle','rb') as handle:
#    y = pickle.load(handle)
#
#print y


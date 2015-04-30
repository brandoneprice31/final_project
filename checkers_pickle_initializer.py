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




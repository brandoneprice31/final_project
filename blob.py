# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:39:58 2015

@author: brandoneprice31
"""

import pickle

with open('checkers_dict.pickle','rb') as handle:
    table = pickle.load(handle)

print len(table)
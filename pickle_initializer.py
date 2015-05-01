'''
CS 51
Tic Tac Toe Program
by Vincent Chow, Stephen Albro, Peter Hickman, & Brandon Price
'''
'''
pickle_initializer.py exists for the sole purpose of replacing whatever is in the
stored pickle file with an empty dictionary. This file is run when we wish to initialize or
clear our current pickle file to test our learning algorithm. 
'''

import pickle

d = {}
# Dump the empty dictionary into the pickle file. 
with open('dict.pickle', 'wb') as handle:
    pickle.dump(d, handle)

# That's all folks.

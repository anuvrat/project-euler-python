'''
Created on Aug 1, 2013

@author: anuvrat
'''
from collections import Counter

n = 0
seq_counts = {}
smallest_cube = {}

loop = True
while( loop ):
    n += 1
    cube = n ** 3
    digits = str( Counter( str( cube ) ) )
    if digits not in seq_counts:
        seq_counts[digits] = 0
        smallest_cube[digits] = cube
    seq_counts[digits] = seq_counts[digits] + 1
    if seq_counts[digits] == 5:
        print( cube, seq_counts[digits], smallest_cube[digits] )
        loop = False

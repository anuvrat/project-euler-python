'''
Created on Aug 1, 2013

@author: anuvrat
'''
from utils.number_utils import isPentagonal, getPentagonal

loop = True

jIdx = 1
while(loop):
    jIdx += 1
    pj = getPentagonal( jIdx )
    
    for kIdx in range( jIdx - 1, 0, -1 ):
        pk = getPentagonal( kIdx )

        if isPentagonal( pj - pk ) and isPentagonal( pj + pk ):
            print( jIdx, pj, kIdx, pk, pj - pk )
            loop = False

'''
Created on Jul 27, 2012

@author: anuvrat
'''
from utils.prime_utils import primefactors

# Get the first number that has 4 distinct prime factors
def getStartNumber( startIdx ):
    for num in xrange( startIdx, 10 ** 7, 1 ):
        if len( set( primefactors( num ) ) ) == 4: return num

def checkForNextThree( startIdx ):
    return len( set( primefactors( startIdx + 1 ) ) ) == 4 and len( set( primefactors( startIdx + 2 ) ) ) == 4 and len( set( primefactors( startIdx + 3 ) ) ) == 4

def findConsequtiveIntegers():
    num = 1
    while( True ):
        startIdx = getStartNumber( num )
        if checkForNextThree( startIdx ): return startIdx
        num = startIdx + 1

print findConsequtiveIntegers()

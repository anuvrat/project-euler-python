'''
Created on Jul 27, 2012

@author: anuvrat
'''
from utils.prime_utils import primefactors

def getStartNumber( startIdx ):
    '''
        Get the first number greater than or equal to the startIdx that has 4 distinct prime factors
    '''
    for num in xrange( startIdx, 10 ** 7, 1 ):
        if len( set( primefactors( num ) ) ) == 4: return num

def checkForNextThree( startIdx ):
    '''
        Returns 0 if the next three consecutive numbers all have 4 distinct prime factors.
        If not, then return the difference between the next number to have 4 distinct prime factors and startIdx.
        If none of the 3 numbers have 4 distinct prime factors, then a value of 4 is returned.
    '''
    factors_count = [len( set( primefactors( startIdx + 1 ) ) ), len( set( primefactors( startIdx + 2 ) ) ), len( set( primefactors( startIdx + 3 ) ) ), 4]
    return 0 if factors_count == [4, 4, 4, 4] else factors_count.index( 4 ) + 1

def findConsequtiveIntegers():
    '''
        Find the first 4 consecutive numbers to each have 4 distinct prime factors.
    '''
    startIdx, res = 1, 4
    while( res ):
        startIdx = getStartNumber( startIdx + 1 ) if res == 4 else startIdx + res
        res = checkForNextThree( startIdx )

    return startIdx

print findConsequtiveIntegers()

'''
Created on Oct 17, 2013

@author: anuvrat
'''
from fractions import gcd

def getCountOfFractions():
    return sum( 1 for d in range( 5, 12001 ) for n in range( int( d / 3 ) + 1, int( d / 2 ) + 1 ) if gcd( n, d ) == 1 )

if __name__ == '__main__':
    print( getCountOfFractions() )

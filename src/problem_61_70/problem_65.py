'''
Created on Oct 16, 2013

@author: anuvrat
'''
from misc.memoize import Memoize

@Memoize
def getA(idx):
    return 2 * ( idx + 1 ) / 3 if idx % 3 == 2 else 1

@Memoize
def getNumerator( idx, c ):
    if idx == 1: return c
    elif idx == 2: return getA( 1 ) * c + 1

    t = getA( idx - 1 ) * getNumerator( idx - 1, c ) + getNumerator( idx - 2, c )
    return t

if __name__ == '__main__':
    num = getNumerator( 100, 2 )
    sumNum = 0
    while num > 0:
        sumNum += num % 10
        num = int( num / 10 )

    print( sumNum )

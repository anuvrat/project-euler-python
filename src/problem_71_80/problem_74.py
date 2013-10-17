'''
Created on Oct 17, 2013

@author: anuvrat
'''
import math
from misc.memoize import Memoize
from misc.numberTools import getDigitsIn

@Memoize
def getFactorial( num ):
    return math.factorial( num )

@Memoize
def getFactorialOfDigits( num ):
    return sum ( getFactorial( digit ) for digit in getDigitsIn( num ) )

def getChainFor( num, chain, chainLengths ):
    if len( chain ) > 60: return None, None
    if chainLengths[num] > 0: return chain, chainLengths[num] - 1
    val = getFactorialOfDigits( num )
    if val in chain: return chain, 0

    chain.append( val )
    return getChainFor( val, chain, chainLengths )

def updateChainLengths(chain, chainLengths, length):
    for item in chain:
        if chainLengths[item] > 0: break
        chainLengths[item] = length
        length -= 1
    return chainLengths

if __name__ == '__main__':
    chainLengths = [0] * 3000000
    for i in range(1000000):
        ( chain, subLength ) = ( [], chainLengths[i] ) if chainLengths[i] > 0 else getChainFor( i, [i], chainLengths )
        if chain == None: continue
        chainLengths = updateChainLengths( chain, chainLengths, len( chain ) + subLength )

    print ( sum( n == 60 for n in chainLengths ) )

'''
Created on Oct 16, 2013

@author: anuvrat
'''
from misc.numberTools import getDigitsIn, getNumberFrom
from utils.prime_utils import is_probable_prime


def getPattern5():
    return [[1, 0, 0, 0, 1],
            [0, 1, 0, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1]]

def getPattern6():
    return [[1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 1],
            [0, 0, 0, 1, 1, 1]]

def generateNumbers( pattern, numDigits ):
    numbers = []
    for i in range(10):
        if pattern[0] == 0 and i == 0: continue

        nIdx, num = 0, []
        for p in pattern:
            if p == 1:
                num.append( numDigits[nIdx] )
                nIdx += 1
            else:
                num.append( i )
        numbers.append( getNumberFrom( num ) )
    return numbers

def getSmallestPrime():
    for num in range( 11, 1000, 2 ):
        if num % 5 == 0: continue

        numDigits = getDigitsIn(num)
        for pattern in getPattern5() if num < 100 else getPattern6():
            numbers = generateNumbers( pattern, numDigits )
            
            size = len( numbers )
            for number in numbers:
                if not is_probable_prime( number ):
                    size -= 1
                    if size < 8: break

            if size == 8:
                return numbers[0]

if __name__ == '__main__':
    print( getSmallestPrime() )

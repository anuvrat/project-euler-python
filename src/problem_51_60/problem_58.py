'''
Created on Jul 27, 2012

@author: anuvrat
'''
from utils.prime_utils import is_probable_prime

def primedSpiral():
    '''
        Returns the side length of the first spiral for which the number of primes along the diagonals are less than 10%
    '''
    primes_count, n = 0, 2
    while( True ):
        length = ( n << 1 ) - 1
        sq = length ** 2
        for i in xrange( 0, ( n - 1 ) << 3, ( n - 1 ) << 1 ):
            if is_probable_prime( sq - i ): primes_count += 1

        if primes_count * 10 < ( ( length << 1 ) + 1 ): return length
        n += 1

print primedSpiral()

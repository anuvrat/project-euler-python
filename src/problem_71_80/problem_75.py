'''
Created on May 13, 2013

@author: anuvrat
'''
import math
from fractions import gcd

def main( limit ):
    triplets = limit * [0]
    for m in xrange( 2, int( math.sqrt( limit / 2 ) ), 1 ):
        for n in xrange( 1, m, 1 ):
            if ( m - n ) % 2 == 1 and gcd( m, n ) == 1:
                p = 2 * m * ( m + n )
                if p > limit: break
                for idx in xrange( p, limit, p ): triplets[idx] += 1

    print( sum( n == 1 for n in triplets ) )

main( 1500000 )

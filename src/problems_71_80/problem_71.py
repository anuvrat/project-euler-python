
'''
Created on Sep 8, 2012

@author: anuvrat
'''

from fractions import Fraction
import math

l = []
for d in range( 7, 1000000 ):
    print( d )
    digits = int( math.log10( d ) ) + 1
    bb = 10 ** digits
    aa = int( 3 * bb / 7 )
    begin = int( ( ( aa - 1 ) / bb ) * d )
    end = int( ( ( aa + 1 ) / bb ) * d )
    l.extend( [Fraction( k / d ).limit_denominator() for k in range( begin, end + 2 )] )
    l = list( set( l ) )
    l.sort()
    idx = l.index( Fraction( 3, 7 ) )
    l = l[idx - 1 : idx + 1]
    print( l )

l = list( set( l ) )
l.sort()

print( l[l.index( Fraction( 3 , 7 ) ) - 1] )

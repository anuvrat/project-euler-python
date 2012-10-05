'''
Created on Sep 28, 2012

@author: anuvrat
'''
from utils.prime_utils import totient, primesfrom2to
from utils.memoize import Memoize

@Memoize
def totient_chain_length( n ):
    if n in range( 21 ): return ( 1, 1, 2, 3, 3, 4, 3, 4, 4, 4, 4, 5, 4, 5, 4, 5, 5, 6, 4, 5, 5 )[n]
    return 1 + totient_chain_length( totient( n ) )

total = 0
for prime in primesfrom2to( 40000000 ):
    if prime < 9000000: continue
    if totient_chain_length( prime - 1 ) == 24: total += prime

print( total )

'''
Created on Jun 30, 2012

@author: anuvrat
'''
from utils.prime_utils import is_probable_prime

squares = [2 * x * x for x in range( 1, 1000000 )]

def can_be_written( odd_composite ):
    for square in squares:
        if is_probable_prime( odd_composite - square ): return True

for odd_composite in xrange( 9, 10 ** 9, 2 ):
    if not is_probable_prime( odd_composite ) and not can_be_written( odd_composite ): break

print odd_composite

'''
Created on Jul 27, 2012

@author: anuvrat
'''
from utils.prime_utils import totient, is_probable_prime

max_ratio, max_number = 0.0, 0
for n in xrange( 1, 10 ** 6, 1 ):
    if is_probable_prime( n ): continue
    ratio = n * 1.0 / totient( n )
    if ratio > max_ratio:
        max_ratio = ratio
        max_number = n

print max_number

'''
Created on Jun 30, 2012

@author: anuvrat
'''
import numpy
import random
from utils.number_utils import gcd
from collections import Counter

def primesfrom2to( n ):
    """
        Input n>=6, Returns a array of primes, 2 <= p < n
        http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """
    sieve = numpy.ones( n / 3 + ( n % 6 == 2 ), dtype = numpy.bool )
    for i in xrange( 1, int( n ** 0.5 ) / 3 + 1 ):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[       k * k / 3     ::2 * k] = False
            sieve[k * ( k - 2 * ( i & 1 ) + 4 ) / 3::2 * k] = False
    return numpy.r_[2, 3, ( ( 3 * numpy.nonzero( sieve )[0][1:] + 1 ) | 1 )]

def is_probable_prime( n, trials = 5 ):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n < 2: return False
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod( d, 2 )
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert( 2 ** s * d == n - 1 )

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite( a ):
        if pow( a, d, n ) == 1:
            return False
        for i in range( s ):
            if pow( a, 2 ** i * d, n ) == n - 1:
                return False
        return True # n is definitely composite

    for i in range( trials ):
        a = random.randrange( 2, n )
        if try_composite( a ):
            return False

    return True # no base tested showed n as composite

smallprimeset = set( primesfrom2to( 100000 ) )
smallprimes = ( 2, ) + tuple( n for n in xrange( 3, 1000, 2 ) if n in smallprimeset )

# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollard_brent( n ):
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3

    y, c, m = random.randint( 1, n - 1 ), random.randint( 1, n - 1 ), random.randint( 1, n - 1 )
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range( r ):
            y = ( pow( y, 2, n ) + c ) % n

        k = 0
        while k < r and g == 1:
            ys = y
            for i in range( min( m, r - k ) ):
                y = ( pow( y, 2, n ) + c ) % n
                q = q * abs( x - y ) % n
            g = gcd( q, n )
            k += m
        r *= 2
    if g == n:
        while True:
            ys = ( pow( ys, 2, n ) + c ) % n
            g = gcd( abs( x - ys ), n )
            if g > 1:
                break

    return g

def primefactors( n, sort = False ):
    factors = []

    limit = int( n ** .5 ) + 1
    for checker in smallprimes:
        if checker > limit: break
        while n % checker == 0:
            factors.append( checker )
            n //= checker
            limit = int( n ** .5 ) + 1
            if checker > limit: break

    if n < 2: return factors
    else :
        factors.extend( bigfactors( n, sort ) )
        return factors

def bigfactors( n, sort = False ):
    factors = []
    while n > 1:
        if is_probable_prime( n ):
            factors.append( n )
            break
        factor = pollard_brent( n )
        factors.extend( bigfactors( factor, sort ) ) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort: factors.sort()
    return factors

totients = {}
def totient( n ):
    if n == 0: return 1

    try: return totients[n]
    except KeyError: pass

    tot = 1
    for p, exp in Counter( primefactors( n ) ).items():
        tot *= ( p - 1 ) * p ** ( exp - 1 )

    totients[n] = tot
    return tot

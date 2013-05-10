'''
Created on Jun 30, 2012

@author: anuvrat
'''
import itertools, operator
from memoize import Memoize
import math

def gcd( a, b ):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

def lcm( a, b ):
    return abs( a * b ) // gcd( a, b )

def all_factors( prime_dict ):
    '''
        print sorted(all_factors({2:3, 3:2, 5:1}))
    '''
    series = [[p ** e for e in range( maxe + 1 )] for p, maxe in prime_dict.items()]
    for multipliers in itertools.product( *series ):
        yield reduce( operator.mul, multipliers )

def divisors( factors ) :
    """
    Generates all divisors, unordered, from the prime factorization.
    divisors([2,2,2,3,3,5])
    """
    ps = sorted( set( factors ) )
    omega = len( ps )

    def rec_gen( n = 0 ) :
        if n == omega :
            yield 1
        else :
            pows = [1]
            for j in xrange( factors.count( ps[n] ) ) :
                pows += [pows[-1] * ps[n]]
            for q in rec_gen( n + 1 ) :
                for p in pows :
                    yield p * q

    for p in rec_gen() :
        yield p

def factor( n ):
    a, r = 1, [1]
    while a * a < n:
        a += 1
        if n % a: continue
        b, f = 1, []
        while n % a == 0:
            n //= a
            b *= a
            f += [i * b for i in r]
        r += f
    if n > 1: r += [i * n for i in r]
    return r

def numberOfDigits( n ):
    return math.floor( math.log10( n ) + 1 )

@Memoize
def firstDigitsOfFib( n, d ):
    """
        For the fibonacci number Fib(n), return the first d digits
    """
    # temp = log( (phi ^ n) / sqrt(5) )
    # => temp = n * log(phi) - log(sqrt(5))
    temp = n * 0.20898764024997873 - 0.3494850021680094
    return int( pow( 10, temp - int( temp ) + d - 1 ) )

@Memoize
def isPandigital( n ):
    digits, count = 0, 0

    while n > 0:
        lastDigit = n % 10
        if not lastDigit: return False

        tmp = digits
        digits |= 1 << ( int )( ( lastDigit ) - 1 )
        if tmp == digits: return False

        count += 1
        n /= 10

    return digits == ( 1 << count ) - 1

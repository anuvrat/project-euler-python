'''
Created on May 22, 2013

@author: anuvrat
'''
from utils.prime_utils import is_probable_prime
from fractions import gcd

def A( n ):
    if is_probable_prime( n ) or gcd( n, 10 ) != 1: return None

    r, k = 11111, 5
    while True:
        if not r % n: break

        r = r * 10 + 1
        k += 1

    return k

def main():
    nums = [91, 259, 451, 481, 703]

    num = nums[-1]
    while len( nums ) < 25:
        num += 2
        a = A( num )

        if a and not ( num - 1 ) % a:
            nums.append( num )
            print len( nums )

    print sum( nums )

main()

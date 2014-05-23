'''
Created on May 23, 2014

@author: anuvrat
'''
from utils import prime_utils

LIMIT = 10000000

def check_condition(num):
    t = prime_utils.totient(num)
    return num * 1.0 / t if sorted(str(num)) == sorted(str(t)) else -1

primes = list(prime_utils.primesfrom2to(5000))
primes.reverse()

smallest_ratio = LIMIT
smallest_num = LIMIT
for a in primes:
    max_allowed = LIMIT / a
    for b in (i for i in primes if i <= max_allowed and i > 1000):
        n = a * b
        phi = n - a if a == b else n - (a + b) + 1
    
        if not sorted(str(n)) == sorted(str(phi)): continue
    
        ratio = n * 1.0 / phi
        if ratio < smallest_ratio:
            smallest_ratio = ratio
            smallest_num = n
            print smallest_ratio, smallest_num

print smallest_num        
    
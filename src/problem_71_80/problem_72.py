'''
Created on May 23, 2014

@author: anuvrat
'''
#from utils import prime_utils
#print sum(prime_utils.totient(n) for n in xrange(2, 1000001))

LIMIT = 1000001

phi = [i for i in xrange(LIMIT)]
result = 0
for i in xrange(2, LIMIT):
    if phi[i] == i:
        for j in xrange(i, LIMIT, i):
            phi[j] = phi[j] * (i - 1) / i
    
    result += phi[i]

print result

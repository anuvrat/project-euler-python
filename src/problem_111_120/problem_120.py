'''
Created on Nov 19, 2012

@author: anuvrat
'''

total = 0
for a in xrange( 3, 1001 ):
    total += 2 * a * ( ( a - 1 ) // 2 )

print total

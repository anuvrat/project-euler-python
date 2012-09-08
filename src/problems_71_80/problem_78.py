'''
Created on Sep 8, 2012

@author: anuvrat
'''
class Memoize:
    def __init__( self, f ):
        self.f = f
        self.cache = {}

    def __call__( self, *args ):
        if not args in self.cache:
            self.cache[args] = self.f( *args )
        return self.cache[args]


@Memoize
def sigma_1( n ):
    return sum( filter( lambda k: n % k == 0, range( 1, n + 1 ) ) )

@Memoize
def partitions( n ):
    if n in range( 11 ):
        return ( 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42 )[n]
    else:
        return sum( sigma_1( n - k ) * partitions( k ) for k in range( n ) ) // n

idx = 12
val = partitions( idx )
while not val % 10000 == 0:
    idx += 1
    val = partitions( idx )

print( "For idx " + str( idx ) + " value = " + str( val ) )

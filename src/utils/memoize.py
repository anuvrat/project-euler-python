'''
Created on Sep 28, 2012

@author: anuvrat
'''

class Memoize( object ):
    '''
    classdocs
    '''

    def __init__( self, f ):
        self.f = f
        self.cache = {}

    def __call__( self, *args ):
        if not args in self.cache: self.cache[args] = self.f( *args )
        return self.cache[args]

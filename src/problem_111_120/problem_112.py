'''
Created on Oct 17, 2013

@author: anuvrat
'''

def isNumberOfType( num, decreasing = False ):
    return num == int( "".join( sorted( str( num ), reverse = decreasing ) ) )

def getBouncyNumberWithDensity(density):
    num, bouncy = 1, 0
    while bouncy / num < density:
        num += 1
        if not isNumberOfType( num, True ) and not isNumberOfType( num, False ): bouncy += 1
    return num

if __name__ == '__main__':
    print( getBouncyNumberWithDensity( 0.99 ) )

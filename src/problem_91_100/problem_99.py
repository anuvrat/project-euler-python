'''
Created on Oct 23, 2012

@author: anuvrat
'''
import numpy

max_digits = max_line = line_idx = 0
for line in ( line.rstrip( '\n' ) for line in open( '/Users/anuvrat/git/project-euler-python/resource/problem_99_input.txt' ) ):
    base, exponent = map( int, line.split( ',' ) )
    digits = exponent * numpy.log10( base )
    if digits > max_digits :
        max_digits = digits
        max_line = line_idx
    line_idx += 1

print max_line + 1

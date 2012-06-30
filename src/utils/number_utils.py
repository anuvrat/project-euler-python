'''
Created on Jun 30, 2012

@author: anuvrat
'''

def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

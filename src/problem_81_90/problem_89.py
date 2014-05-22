'''
Created on May 23, 2014

@author: anuvrat
'''
from collections import namedtuple

filename = '/Users/anuvrat/git/project-euler-python/resource/problem_89_input.txt'

Pair = namedtuple('RomanPair', ['i', 'r'])
nums = [Pair(1000, 'M'), Pair(900, 'CM'), Pair(500, 'D'), Pair(400, 'CD'), Pair(100, 'C'), Pair(90, 'XC'),
        Pair(50, 'L'), Pair(40, 'XL'), Pair(10, 'X'), Pair(9, 'IX'), Pair(5, 'V'), Pair(4, 'IV'), Pair(1, 'I')]
romans = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def int_to_roman(num):
    result = []
    for n in nums:
        count = int(num / n.i)
        result.append(n.r * count)
        num -= n.i * count
    return ''.join(result)

def roman_to_int(num):
    num = num.upper()
    val = 0
    for i in range(len(num)):
        value = romans[num[i]]
        # If the next place holds a larger number, this value is negative
        if i+1 < len(num) and romans[num[i+1]] > value:
            val -= value
        else: val += value
    return val

letters_saved = 0
with open(filename) as f:
    for line in f:
        line = line.strip()
        val = roman_to_int(line)
        roman = int_to_roman(val)
        print(line, str(val), roman, str(len(line) - len(roman)))
        letters_saved += len(line) - len(roman)

print(letters_saved)

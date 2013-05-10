'''
Created on May 9, 2013

@author: anuvrat
'''
from utils.number_utils import isPandigital, firstDigitsOfFib

def main():
    f1, f2, idx = 1, 1, 2
    while idx < 2749 or not isPandigital( f2 % 1000000000 ) or not isPandigital( firstDigitsOfFib( idx, 9 ) ):
        f1, f2 = f2, f1 + f2
        idx += 1

    print( idx )

main()

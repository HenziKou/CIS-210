'''
Project 5.1: Number Conversions Revisited
    "Recursive Binary Encoding"
CIS 210

Author: Henzi Kou
Credits: stacksOverflow

Write and implement recursive algorithm to implement decimal (base 10)
number to binary conversion.
    Practice with:
        - Systematic testing of functions
        - Recursive functions/algorithms
'''

import doctest



def dtob(n, b):
    '''
    (int, int) -> str

    Converts a non-negative integer n, to any base b.

    Examples:
    >>> dtob(4, 2)
    '100'
    >>> dtob(0, 2)
    '0'
    >>> dtob(1, 10)
    '1'
    >>> dtob(32156, 16)
    '713912'
    >>> dtob(853169, 32)
    '261517'
    '''
    
    assert n >= 0
    assert isinstance(n, int)

    if n == 0:
        strRep = '0'
    else:
        strRep = ''
        next_n = n
        while next_n > 0:
            r = next_n % b
            strRep = str(r) + strRep
            next_n = next_n // b

    return strRep




def btod(strRep, b):
    '''
    (str, int) -> int

    Converts the base string given by strRep to base 10 decimal integer.

    Examples:
    >>> btod('100', 2)
    4
    >>> btod('11111', 2)
    31
    '''

    # type checking
    #for bit in b:
    #    assert bit in '01'

    '''
    # or
    for bit in b:
        if bit not in '01':
            raise Exception('Not a binary string.')

    # or
    pyd = int(b, 2)     # run-time error for non-binary string
    '''    

    dn = 0
    bctr = len(strRep) - 1
    for bit in strRep:
        dn += int(bit) * (2 ** bctr)
        bctr -= 1

    return dn



# RECURSIVE FORMULA FOR INT TO ANY BASE

def dtobr(n, b):
    '''
    (int, int) -> str

    Implements a recursive algorithm to convert a non-negative integer to its
    base representation.

    Max base representation is 36.

    n ---> non-negative integer in base 10
    b ---> base to convert to

    Examples:
    >>> dtobr(27, 2)
    '11011'
    >>> dtobr(0, 3)
    '0'
    >>> dtobr(1, 5)
    '1'
    >>> dtobr(1453, 16)
    '51013'
    >>> dtobr(3600000, 36)
    '255280'
    '''

    assert n >= 0
    assert isinstance(n, int)
    
    convertStr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if n == 0:
        return '0'
    elif n < b:
        return convertStr[n]
    else:
        return dtobr(n // b, b) + str(n % b)

    return None




def main():
    '''
    () -> None

    Check binary conversion functions by encoding and decoding number
    '''

    dec = int((input('Enter non-negative integer: ')))
    base = int(input('Enter a base: '))
    
    # convert to binary
    b = dtob(dec, base)
    print('Binary format is {}'.format(b))

    # convert back to decimal
    checkd = btod(b, base)
    print('Back to decimal: {}'.format(checkd))

    # convert back to binary with recursive formula
    checkR = dtobr(dec, base)
    print('Back to binary format using recursive formula is {}'.format(checkR))
    
    return None
    


print(doctest.testmod())



if __name__ == '__main__':
    main()















# THERE IS EXTRA CREDIT
'''
Generalize function 'dtob', 'dtobr', and 'btod' to convert decimal (base 10)
numbers to any base from binary to hexadecimal (base 16).

HINT: For what cases are the decimal and binary representations the same?
'''





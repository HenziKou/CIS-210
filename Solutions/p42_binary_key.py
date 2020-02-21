'''
Binary numbers.

CIS 210 F17 Project 4-2.

Author: [Solution]

Credits:  N/A

"Encode" and "decode" decimal numbers to
binary representations.

Credits: N/A
'''
import doctest

def dtob(n):
    '''(int) -> str

    Convert non-negative integer n to binary string.

    >>> dtob(4)
    '100'
    >>> dtob(0)
    '0'
    >>> dtob(1)
    '1'
    >>> dtob(2)
    '10'
    >>> dtob(27)
    '11011'
    >>> dtob(44)
    '101100'
 
    '''
    assert n >= 0
    assert isinstance(n, int)

    if n == 0:
        b = '0'
    else:
        b = ''
        next_n = n
        while next_n > 0:
            r = next_n % 2
            b = str(r) + b
            next_n = next_n // 2

    return b

def btod(b):
    '''(str) -> integer

    Convert binary string to decimal integer.

    >>> btod('100')
    4
    >>> btod('11111')
    31
    >>> btod('0000')
    0
    >>> btod('11011')
    27
    >>> btod('101100')
    44
    '''
    # type checking
    for bit in b:
        assert bit in '01'
    '''
    # or
    for bit in b:
        if bit not in '01':
            raise Exception('Not a binary string.')

    # or
    pyd = int(b, 2)     # run-time error for non-binary string
    '''    
    dn = 0
    bctr = len(b) - 1
    for bit in b:
        dn += int(bit) * (2**bctr)
        bctr -= 1

    return dn

def main():
    '''() -> None

    check binary conversion functions
    by encoding and decoding number
    '''
    d = int((input('Enter non-negative integer: ')))
    b = dtob(d) # convert to binary
    print('Binary format is {}'.format(b))

    checkd = btod(b) # convert back to decimal
    print('Back to decimal: {}'.format(checkd))
    
    return None

'''
if __name__ == '__main__':
    main()
'''   

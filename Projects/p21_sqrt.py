'''
    CIS 210
    Approximate Square Root

    Author: Henzi Kou
    Credits: w3resource

    Approximates the square root of a number using an algorithm and then
    compares the result to the Python square root function result.
'''

from math import *

def mysqrt(n, k):
    '''
    By using the Babylonian square root method, this generates an approximate
    square root for any given num. Additionally the program will run the
    program a certain amount of times based on the inputed iterations, k.

    Some examples:
    >>> mysqrt(25, 5)
    5.000023178253949
    
    >>> mysqrt(25, 10)
    5.0
    
    >>> mysqrt(100, 10)
    10.0

    >>> mysqrt(625, 10)
    25.0

    >>> mysqrt(10000, 8)
    101.20218365353946

    >>> mysqrt(10000, 10)
    100.00000025490743

    >>> mysqrt(10000, 11)
    100.0
    '''

    i = 0
    guess = 1
    while i < k:
        new_guess = (0.5) * (guess + (n / guess))
        i = i + 1
        guess = new_guess

    return new_guess
    


def sqrt_compare(num, iterations):
    '''
    By using the Python function from the math module, it will give its
    approximation of the square root for any given n. The program also has
    an additional parameter of number of iterations when asked along with the
    value. Then with Python's result it will compare the answer with that of
    the 'mysqrt' function that uses an ancient Babylonian method to calculate
    the square root of a number.

    sqrt_compare should yield the following, for example:
    
    >>> sqrt_compare(10000, 8)
    For 10000 using 8 iterations:
    mysqrt value is: 101.20218365353946
    math lib sqrt value is: 100.0
    This is a 1.2 percent error.
    '''

    sval1 = mysqrt(num, iterations)
    sval2 = sqrt(num)

    # determine the error compared to math module sqrt
    diff = abs(sval2 - sval1)
    err = (diff / sval2) * 100 

    # format for reporting
    err = round(err, 2)
    
    print('For ', num, 'using', iterations, 'iterations:')
    print('mysqrt value is: ', sval1)
    print('math lib sqrt value is: ', sval2)
    print('This is a', err, 'percent error.')

    return None



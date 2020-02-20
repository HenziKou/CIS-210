'''
CIS 210
Monte Pi Part 1

Author: Henzi Kou
Credits:

Approximate the square root of pi using Monte Carlo algorithm.
'''

import random
import math

def montePi(numDarts):
    '''
    (int) -> float

    The parameter 'numDarts' generates the number of times the
    approximating pi process should be ran. The funciton 'montePi' will
    return the approximate value for pi that is generated by the function.

    The random element in Monte Carlo algorithms means that the examples of
    function use for 'montePi' may not be replicable.
    
    montePi should return:
    >>> montePi(100)
    3.08
    >>> montePi(100000)
    3.143072
    >>> montePi(10000000)
    3.1418752
    '''

    # initialize accumulator variable
    inCircle = 0   # ---> CHECK TO SEE IF THIS IS TO CALL 'isInCircle'
    for i in range(numDarts):
        # throw the dart
        x = random.random()
        y = random.random()
        # check location
        d = math.sqrt(x ** 2 + y ** 2)

        # it's in the circle
        if d <= 1:
            # increment accumulator variable
            inCircle += 1

    # approximating pi
    pi = inCircle / numDarts * 4

    return pi


def isInCircle(x, y, r):
    '''
    (float, float, float) -> str

    Will be called on by the function 'montePi'. *TODO*
    
    Returns 'True' if the input point is inside the circle centered at point
    (0, 0) with radius r, and 'False' otherwise.

    isInCircle should return:
    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False
    '''

    # if, elif, else statements
    
    if (x ** 2 + y ** 2 <= r):
        return True
    else:
        return False
    
    return None
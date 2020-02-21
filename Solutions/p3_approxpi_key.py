'''
Approximating pi.  CIS 210F17 Project 3-1

Author: [Solution]

Credits:  Based on code in Miller and Ranum text.

Approximate pi using a Monte Carlo simulation.

Practice:
-designing Python functions
-revising code
-good programming style
-Python user-defined functions 
-numeric data type and operators
-Python expressions
-variable assignment
-loop (use Python for statement to implement repeat)
-functions return values; may have side effects (e.g., print)
-importing modules/Python standard library

-accumulator pattern
-Boolean data type/operations
-conditional statements
-math, random, and turtle graphics modules
'''
import math
import random
from turtle import *

def isInCircle(x, y, r):
    '''(number, number, number) -> Boolean

    Returns True if point (x, y) is in
    the circle with radius r.

    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False
    '''
    d = math.sqrt(x**2 + y**2)
    isIn = d <= r

    return isIn

def montePi(numDarts):
    '''
    (integer) -> float

    Uses a Monte Carlo algorithm (looping
    numdarts times) to generate an
    approximate value for pi, which is
    returned.

    Calls:  isInCircle

    Due to randomness in the algorithm,
    function output may vary somewhat
    from function call to function call.
    
    >>> montePi(1000)
    3.168
    >>> montePi(100000)
    3.13572
    >>> montePi(1000000)
    3.141068
    '''   
    inCircle = 0

    # throw the darts and check whether
    # they landed on the dart board;
    # keep count of those that do.
    
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        if isInCircle(x, y, 1):
            inCircle += 1

    approxPi = inCircle/numDarts * 4
    
    return approxPi

def showMontePi(numDarts):
    '''
    (integer) -> float

    Uses a Monte Carlo algorithm (looping
    numdarts times) to generate an
    approximate value for pi, which is
    returned.

    The results of numDarts
    throws are displayed using turtle graphics.
    The difference between the approximate
    value of pi and the math library value
    is reported.

    Calls:  isInCircle

    Due to randomness in the algorithm,
    function output may vary somewhat
    from function call to function call.
    
    >>> showMontePi(100)
    <graphical output>
    With 100 iterations:
    my approximate value for pi is:  3.28
    math lib pi value is:  3.141592653589793
    This is a 4.41 percent error.

    3.28
    >>> showMontePi(1000)
    <graphical output>
    With 1000 iterations:
    my approximate value for pi is:  3.22
    math lib pi value is:  3.141592653589793
    This is a 2.5 percent error.

    3.22
    '''
    # set up canvas and turtle
    # to animate the algorithm;
    # draw x, y axes
    
    wn = Screen()
    wn.setworldcoordinates(-2, -2, 2, 2)

    speed(0); hideturtle()
    penup()

    goto(-1, 0)
    pendown()
    goto(1, 0)
    penup()
    goto(0, 1)
    pendown()
    goto(0, -1)
    penup()
    goto(0, -1)
    #pendown()
    #circle(1, steps=100)

    # pen should stay up for drawing darts
 
    inCircleCt = 0

    # throw the darts and check whether
    # they landed on the dart board and
    # keep count of those that do   
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        # show the dart on the board
        if isInCircle(x, y, 1):
            inCircleCt += 1
            color('blue')
        else:
            color('red')

        goto(x, y)
        dot()

    # calculate approximate pi
    approxPi = inCircleCt/numDarts * 4

    # determine the error compared to math module sqrt
    diff = abs(math.pi - approxPi)
    err = (diff / math.pi) * 100 

    # format for reporting
    err = round(err, 2)
    
    print('With', numDarts, 'iterations:')
    print('my approximate value for pi is: ', approxPi)
    print('math lib pi value is: ', math.pi)
    print('This is a', err, 'percent error.')
    print()

    wn.exitonclick()

    return approxPi

def showMontePi_demo(numDarts, draw=False):
    '''
    (integer, [bool]) -> float

    This version of showMontePi uses a
    default parameter so the caller can
    specify whether to show the graphical
    output and report on the result.

    Other ideas for a better showMontePi -
    move the drawing code (setup, show darts)
    into auxiliary functions - add another
    parameter so drawing and reporting can
    be controlled separately.

    Calls:  isInCircle

    Due to randomness in the algorithm,
    function output may vary somewhat
    from function call to function call.
    
    >>> showMontePi_demo(100, True)
    <graphical output>
    With 100 iterations:
    my approximate value for pi is:  3.28
    math lib pi value is:  3.141592653589793
    This is a 4.41 percent error.

    3.28
    >>> showMontePi_demo(1000)
    <no graphical output>
    With 1000 iterations:
    my approximate value for pi is:  3.22
    math lib pi value is:  3.141592653589793
    This is a 2.5 percent error.

    3.22
    '''
    # set up canvas and turtle
    # to animate the algorithm;
    # draw x, y axes

    if draw:
    
        wn = Screen()
        wn.setworldcoordinates(-2, -2, 2, 2)

        speed(0); hideturtle()
        penup()

        goto(-1, 0)
        pendown()
        goto(1, 0)
        penup()
        goto(0, 1)
        pendown()
        goto(0, -1)
        penup()
        goto(0, -1)
        #pendown()
        #circle(1, steps=100)

        # pen can stay up for drawing darts

    inCircleCt = 0

    # throw the darts and check whether
    # they landed on the dart board and
    # keep count of those that do   
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        # show the dart on the board
        cflag = isInCircle(x, y, 1)
        
        if cflag:
            inCircleCt += 1

        if draw:
            if cflag:
                color('blue')
            else:
                color('red')
            
            goto(x, y)
            dot()

    # calculate approximate pi
    approxPi = inCircleCt/numDarts * 4

    # determine the error compared to
    # math module sqrt
    if draw:
        diff = abs(math.pi - approxPi)
        err = (diff / math.pi) * 100 

    # format for reporting
        err = round(err, 2)
    
        print('With', numDarts, 'iterations:')
        print('my approximate value for \u03C0 is: ', approxPi)
        print('math lib \u03C0 value is: ', math.pi)
        print('This is a {}% error.'.format(err))
        print()

        wn.exitonclick()

    return approxPi

print(isInCircle(0, 0, 1))
print(isInCircle(.5, .5, 1))
print(isInCircle(1, 2, 1))
print()

print(montePi(100))
print(montePi(100000))
print(montePi(10000000))
print()

showMontePi(1000)
print()
#showMontePi_demo(100, True)





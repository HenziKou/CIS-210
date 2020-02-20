'''
Approximating pi.  CIS 210 F17 Project 3-2
Starter Code for showMontePi

Author: Henzi Kou

Credits: Based on code on p.78 Miller and Ranum text.

Approximate pi using a Monte Carlo simulation.
Then add graphics to visualize simulation.
'''

from turtle import *
import math
import random

def showMontePi(numDarts):
    '''
    (int) -> string with float and a Python Turtle animation

    Displays a graphical visualization of the algorithm Monte Carlo.

    Click on finished Python Turtle Graphics to close the program.
    

    Given an integer, program run that amount of times to approximate
    pi and compares the value to Python pi value. Prints several lines of
    statements to calculate the percent error of the Monte Carlo algorithm
    to the math library pi value.

    The program should yield the following,
    >>> showMontePi(1000)
    With 1000 iterations:
    my approximate value for pi is: 3.104
    math lib pi value is: 3.141592653589793
    This is a 1.2 percent error.
    '''
    # set up canvas and turtle
    # to animate the algorithm;
    # draw x, y axes
    
    wn = Screen()
    wn.setworldcoordinates(-2, -2, 2, 2)

    speed('fastest'); hideturtle()
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

    # pen should stay up for drawing darts
 
    inCircleCt = 0

    # throw the darts and check whether
    # they landed on the dart board and
    # keep count of those that do   
    for i in range(numDarts):
        x = random.random()
        y = random.random()

    # Revise code to call new isInCircle function.
    # See Project 3-1 and 3-2 specifications.

        d = math.sqrt(x**2 + y**2)

        # show the dart on the board
        if d < 1:
            inCircleCt += 1
            color('blue')
        else:
            color('red')

        goto(x, y)
        dot()

    # calculate approximate pi
    approxPi = inCircleCt/numDarts * 4

    # ADD CODE HERE to compare approxPi to math.pi
    # See Project 3-2 specification
    pythPi = math.pi
    diff = abs((approxPi - pythPi) / pythPi)
    percError = round((diff * 100), 2)

    wn.exitonclick()

    print("With ", numDarts, "iterations:")
    print("my approximate value for pi is:", approxPi)
    print("math lib pi value is:", pythPi)
    print("This is a ", percError, "percent error.")

    return None

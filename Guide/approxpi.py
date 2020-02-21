'''
Approximating Pi. Project 2, Part 2. CIS 210
Author: Quinn Milionis
Credits: Bradley N. Mililer and David L. Ranum
A funciton that approximates pie using
the Monte Carlo simulation, as well as displys a
graphical animation of the algorithm and compares
the approximated pi to the stored pi value in
python libraries.
'''

import math
: import random
import turtle

def isinCircle_stub (x,y,r):
    """
Given x and y coordinates and a radius of a circle
centered on 0,0 will return either true or false
depending on if the point would lie inside the
circle.
>>> isinCircle (1,2,4):
>>> True
"""
    pass
    #return True or False

def isinCircle (x,y,r):
    """
Given x and y coordinates and a radius of a circle
centered on 0,0 will return either true or false
depending on if the point would lie inside the
circle.
>>> isinCircle (1,2,4):
>>> True
"""
    d = math.sqrt(x**2 + y**2)

    if d <= r:
        return True 
    else:
        return False

#isinCircle(3,7,8)



def showMontePi (numDarts):
    """
int -> float
given the number of "darts", will estimate
the value of pi, as well as provide a graphical
animation of this algorithm. Afterward, it will
compare the estimated pi value to the one stored
in Python math libaries.
>>> showMontePi (100)
With 100 iterations:
my approximate value for pi is: 3.16
math lib pi value is: 3.141592653589793 
This is a 0.59 %  error.
"""
    wn = turtle.Screen()
    drawingT = turtle.Turtle()
    wn.setworldcoordinates(-2,-2,2,2)
    drawingT.speed(0)
    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)
    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)
    drawingT.up()
    
    inCircle = 0

    for i in range (numDarts):
        x = random.random()
        y = random.random()
        
        drawingT.goto(x,y)
        if isinCircle (x,y,1) == True:
            inCircle += 1
            drawingT.color("blue")
        else:
            drawingT.color("red")

        drawingT.dot()

    pi = inCircle/numDarts * 4
    # My exitonclick function wasnt working, but I
    # did some research and it looks like I might
    # have to change a preference in my Idle
    # system files. I'm going to try to get it working
    # later, but am submitting this program as is. 
    wn.exitonclick()

    piTwo = math.pi
    error = ((pi - piTwo)/piTwo)*100
    errorRound = round(error,2)
    
    print(" With",numDarts,"iterations:\n",
          "my approximate value for pi is:", pi,"\n",
          "math lib pi value is:", piTwo,"\n",
          "This is a",errorRound,"%  error.")
    return pi




showMontePi(100)

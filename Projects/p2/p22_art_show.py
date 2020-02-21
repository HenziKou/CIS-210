'''
    CIS 210
    Art Show

    Author: Henzi Kou
    Credits: N/A

    Using Python program, Turtle to create a design or drawing.
'''

from turtle import *


def art_show():
    '''
    Running the program will call on the functions using the program Turtle
    to draw an image of a rainbow behind a sun.

    For example:
    >>> art_show()
    'returns an image of a rainbow behind a sun that is drawn by Turtle program'
    '''
    rainbow_colors = ("red", "orange", "yellow", "greenyellow", "aquamarine",
                   "skyblue", "royalblue", "blueviolet", "indigo")
    reset()
    Screen()
    up()
    goto(-320, -260)
    width(68)
    speed(5)

    for rcolor in rainbow_colors:
        color(rcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)

    width(25)
    color("gold")
    goto(0,-170)
    down()

    begin_fill()
    circle(170)
    end_fill()
    penup()
    

    goto(0, 300)

    return None

from turtle import *
from random import *
speed(0)

def draw_octagon(size):
    for i in range (8):
            forward(size)
            right(45)

def draw_star(size):
    angle = 140
    for i in range (5):
        forward (size)
        right(angle)
        forward(size)
        right (72 - angle)

def random_jump():
        penup()
        randLocX = randint(-400,400)
        randLocY = randint(-400,400)
        goto(randLocX,randLocY)
        pendown()

def art_show (size, amount):
    """
Given the size and amount of stars, will populate a night sky with stars
of differing colors
returns None
"""

    bgcolor ('black') 
    Num = 0
    width(5)
    for i in range (amount):
        fillList = ('blue', 'yellow', 'red', 'navy', 'magenta')
        colorList = ('light blue', 'dark green', 'pink', 'orange', 'white')
        Num = randint (0,4)
        pencolor (colorList[Num])
        Num = randint (0,4)
        fillcolor(fillList[Num])
        begin_fill()
        draw_star (size)
        #previous ideas to test function, decided that stars were the coolest
        #draw_octagon (size)
        #circle (size)
        end_fill()
        random_jump()
    return None

art_show (20,100)


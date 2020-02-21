# header

def iPrint(msg):

    print("Error diagnostics", msg);

    return None

# math.sqrt(100) ---> The period means to append

# from turtle import ___*___ ---> * imports everything

# import matplotlib as m ---> a way to create a shorthand for m.plot() and
#                             great for really long file names



from turtle import *

def draw_poly(color, thickness, nsides, side_length):
    '''
    (string, int, int, num) -> None

    Draws a polygon to the turtle window

    Examples:
    >>> draw_poly('blue', 5, 6, 100)
    blue hexagon drawn to turtle window
    '''

    pencolor(color)
    pensize(thickness)

    for i in range(nsides):
        forward(side_length)
        left(360/nsides)

    return None


def move_t(x, y):
    penup()
    goto(x, y)
    pendown()


draw_poly('red', 6, 11, 100)
move_t(50, -50)
draw_poly('blue', 2, 4, 200)





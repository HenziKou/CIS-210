from turtle import *
speed (0)

def draw_square(size):
    for i in range (4):
        forward (size)
        right (90)
    



def draw_flower (size):
    begin_fill()
    for i in range (46):
        draw_square (size)
        right(10)
    end_fill()

draw_flower (100)

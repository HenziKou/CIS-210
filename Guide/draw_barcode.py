'''
Drawing a barcode. Project 5, Part 1. CIS 210
Author: Quinn Milinois
Given a zip code (or any other series of numbers),
draws a coresponding barcode complete wth a
check digit at the end
'''



import turtle

turtle.up()
turtle.backward(100)

ENCODINGS = [[1,1,0,0,0],       #index position 0
             [0,0,0,1,1],       #1
             [0,0,1,0,1],       #2
             [0,0,1,1,0],       #3
             [0,1,0,0,1],       #4
             [0,1,0,1,0],       #5
             [0,1,1,0,0],       #6
             [1,0,0,0,1],       #7
             [1,0,0,1,0],       #8
             [1,0,1,0,0]]       #9

SingleLength = 25

def checkDigit (zip):
    """
int -> int
generates a check digit based off
a given zip code. used in the
zipToBar function. 
"""
    sum = 0
    for i in str(zip):
        i = int(i)
        sum = sum + i
    checkDigit = 10 - (sum % 10)
    if checkDigit == 10:
        checkDigit = 0
    return checkDigit
        
    
    
    

def drawBar (digit):
    if digit == 0:
        length = SingleLength
    else:
        length = SingleLength * 2
    turtle.left (90)
    turtle.forward (length)
    turtle.up()
    turtle.backward(length)
    turtle.right(90)
    turtle.forward(10)
    turtle.down()
    
        

def zipToBar (zip):
    """
int -> turtle img/str
given a zipcode, uses turtle graphics to
generate the corresponding bar code, with
the included starting and ending bars, as
well as the checkdigit
returns None

"""
    drawBar (1)
    for i in str(zip):
        i = int(i)
        #print (i)
        for num in ENCODINGS [i]:
        
            drawBar (num)
    for j in ENCODINGS [checkDigit(zip)]:
        drawBar (j)

    drawBar (1)
    return None




    


            
        



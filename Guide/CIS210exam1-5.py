import math

'''
Midterm 1 - Lab 5. CIS 210
Author: Quinn Milionis
'''

for count in range (50,0,-1):
    print (count)

           REMEMBER TO UNCOMMENT THIS BEFORE SUBMITTING    

def isInCircle (x,y,r):
    """
int,int,int -> boolean 
Given the x and y coordinates and radius of a circle
centered on 0,0 will return either true or false
depending on if the point would lie inside the
circle
returns True/False
>>> isinCircle (1,2,4):
>>> True
"""
    d = math.sqrt(x**2 + y**2)

    if d <= r:
        return True 
    else:
        return False


def greet (greeting, name):
    """
str,str -> str 
Given a greeting an a name, prints two greeting
sentenses.
returns None
>>> greet ('hello', 'oregon')
Hello, Oregon.
Oregon, hello.
"""
    # Although not the most elegant solution, this was
    # the way I found to print without having spaces
    # between the varaibles and the punctuation.
    greetingC = greeting + ','
    nameC = name + ','
    greetingP = greeting + '.'
    nameP = name + '.'

    print (greetingC.title(),nameP.title())
    print (nameC.title(),greetingP)
    return None
    
    

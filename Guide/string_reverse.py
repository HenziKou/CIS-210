'''
String Reversal. Project 5, part 2. CIS 210
Author: Quinn Milionis
Defines two functions, one uses recursion to
reverse a string, and the other is iterative.
'''



def strReverseR (string):
    """
str -> str
Given a string, recursively gathers up
the characters in revrse order, unitl there
arent any letters left, in which the function
excutes the return functions and generates
the reversed string. Returns String.
>>> strReverseR('CIS 210')
'012 SIC'
"""
    if string == "":
        return string
    else:
        return string[-1] + strReverseR (string[:-1])



def StrReverseI (string):
    """
str -> str
given a string, generates the reverse of that
string useing an iteration loop inside the for
loop. Returns String.
>>> strReverseI('CIS 210')
'012 SIC'
"""
    ReverseString = ''

    for c in string[::-1]:
        ReverseString += c
    return ReverseString

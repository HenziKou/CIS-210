'''
Square Root. Project 1, Part 2. CIS 210
Author: Quinn Milionis 
Credits: N/A
A function that computues a square root estimation
based on a given number and number of iterations the
equation should run, and then compares the generated
number to the number provided by pythons built in
square root function
'''

from math import sqrt

def sqrt_compare_stub (num, iterations):
    """
interger -> float
Given a number and the number of iterations,
estimates a square root for that number and
compares it to the python scripts generation
of that same number.

>>> sqrt_compare(100, 5)
For  100 using 5 iterations:
my_sqrt value is:  10.032578510960604
math lib sqrt value is:  10.0
This is a 0.33 percent error."""
    pass
    #return none
    

def sqrt_compare (num, iterations):
    """
interger -> float
Given a number and the number of iterations,
estimates a square root for that number and
compares it to the python scripts generation
of that same number

>>> sqrt_compare(100, 5)
For  100 using 5 iterations:
my_sqrt value is:  10.032578510960604
math lib sqrt value is:  10.0
This is a 0.33 percent error."""
    K = 1
    for i in range (iterations):
        K = ((1/2) * (K + (num/K)))

    #return K,sqrt(num)
    sqrt2 = sqrt (num)
    error = (((K - sqrt2)/sqrt2)*100)
    errorRound = round(error,2)

    print(" For ",num," Using", iterations, "iterations:\n",
          "my sqrt value is:", K,"\n",
          "math lib sqrt value is:", sqrt2,"\n",
          "This is a",errorRound,"%  error.")
    return K         
          

sqrt_compare(100,4)



#Project 0.py
'''
Temperature converson. Project 0, CIS 210
Author: Quinn Milionis
Credits: N/A
A function that will convert a given tempterature given
in Celsius to an equilvalent tempterature in Fahrenheit
'''

def ctemp_to_ftemp_stub (ctemp):
     """ (number) --> float
Given the temperature in Celsius, returns
an equilvant temperature in Fahrenheit
>>> ctemp_to_ftemp (100)
212.0
"""
     pass
#    return ftemp



def ctemp_to_ftemp (ctemp):
    """ (number) --> float
Given the temperature in Celsius, returns
an equilvant temperature in Fahrenheit
>>> ctemp_to_ftemp (100)
212.0
"""
    ftemp = ctemp * 9/5 + 32
#    DEBUG
#    print (ftemp)
    return ftemp


#test of function
#print (ctemp_to_ftemp (100))





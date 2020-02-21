#project1.1.py
'''
Cricket Chirps. Project 1, Part 1. CIS 210
Author: Quinn Milonis
Credits: N/A
A function that compututes the tempterature in
degrees fahrenheit based on the number of cricket
chirps in a 25 second interval.
'''

from temperature import ctemp_to_ftemp


def chirps_to_ftemp_stub (chirps):
    """ (number -> float)
Given the number of chirps in a 25 second
interval, prints the equilvalent
temperature in Fahrenheit. Returns None.
>>> chrips_to_ftemp(30)
The estimated temperature based on 30 chirps
in 25 seconds, is 57.2 degrees fahrenheit.
"""
    pass
    return None

def chirps_to_ftemp (chirps):
    """
(number -> float)
Given the number of chirps in a 25 second
interval, prints the equilvalent
temperature in Fahrenheit. Returns None.
>>> chrips_to_ftemp(30)
The estimated temperature based on 30 chirps
in 25 seconds, is 57.2 degrees fahrenheit.
"""
    ctemp = chirps / 3 + 4
    ftemp = ctemp_to_ftemp (ctemp)
    print ("The estimated temperature\nbased on", chirps, "in 25 seconds",
           "\nis", ftemp, "degrees fahrenheit")

chirps_to_ftemp(30)



    


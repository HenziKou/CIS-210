# Pizza Calculator
# Lab 3 Demo - CIS 210

'''
Company:      Size:     Price:
Falling Sky    14        19
Falling Sky    18        27
Pegasus        10        13
Pegasus        14        19
Pegauss        16        24
Dominoes       14        16
Dominoes       16        18



Given a diameter and cost, print (return??) the price per square
inch of the pizza.
'''

import math

def pizza_calc(diameter, cost):
    '''
    (int, float) -> float

    Given a diameter and cost, finds and reports the price per square inch
    of pizza.

    >>> pizza_calc(14, 19)
    Price per square inch: $0.12
    '''

    # find area
    area = get_area(diameter)

    # divide cost by area
    price_per_sqin = cost / area
    price_per_sqin = round(price_per_sqin, 2)

    # report result
    print("Price per square inch: $", price_per_sqin, sep = '')

    # return??? TODO
    return None


def get_area(diameter):
    '''
    (num) -> float
    Finds and returns area of circle with given diameter.

    >>> get_area(1)
    3.14
    '''

    r = diameter / 2
    area = math.pi * (r ** 2)
    return area

    
def find_best_deal(list_of_pizza_info):
    '''

    '''

    pizza1_val = pizza_calc(p1_d, p1_c)

    


'''                          # FILE HEADER
Nature's Thermometer: Cricket Chirps.
CIS 210 F17 Project 1

Author: Henzi Kou

Credits: N/A

Determine the temperature based on cricket
chirps. (Farmers Almanac)
'''

def chirps_to_ctemp(ch25):  #FUNCTION HEADER
    '''(int) -> float       #TYPE CONTRACT
                            #BRIEF DESCRIPTION refers to
                            #PARMS, RETURN VAL
    Return celsius temp estimated based on
    number of cricket chirps in a 25 second
    interval (ch25) - divide by 3 and add 4
    to get the celsius temperature.
                            #EXAMPLES OF USE
    >>> chirps_to_ctemp(48)
    20.0
    >>> chirps_to_ctemp(93)
    35.0
    >>> chirps_to_ctemp(0)
    4.0
    '''

    total = 0
    if ch25 == 0:
        return total + 4
    for i in range(ch25):
        total = (ch25 / 3) + 4

    return total

    
def chirps_to_ftemp(ch14):
    '''(int) -> None

    Print fahrenheit temp estimated based on
    number of cricket chirps in a 14 second
    interval (ch14) - add 40. None value is returned.

    >>> chirps_to_ftemp(0)
    The estimated temperature,
    based on 0 chirps in 14 seconds, is
    40 degrees fahrenheit.
    >>> chirps_to_ftemp(50)
    The estimated temperature,
    based on 50 chirps in 14 seconds, is
    90 degrees fahrenheit. 
    '''

    total = 0

    if ch14 == 0:
        return 40
    
    for i in range(ch14):
        total = ch14 + 40

    return total


'''
Project 6.2: Data Analysis
CIS 210

Author: Henzi Kou
Credits: Textbook

Understand, implement, and revise data analysis and visualization
functions.
    Practice with:
        - Data analysis
        - Python collections (i.e. lists and dictionaries)
'''

import doctest
import turtle


def isEven(n):
    '''
    (int) -> boolean

    Returns a boolean:
        - True if the number n is even
        - False if the number n is odd

    Examples:
    >>> isEven(10)
    True
    >>> isEven(135)
    False
    '''

    assert isinstance(n, int)
    
    if n % 2 == 0:
        return True
    else:
        return False

    return None



def median(alist):
    '''
    (list) -> float

    Computes and returns the median value of a list.

    Examples:
    >>> median([20, 32, 21, 26, 33, 22, 18])
    22
    >>> median([20, 32, 21, 26, 33, 22, 18, 29])
    24.0
    '''

    copylist = alist[:]   # makes a copy using slice operator
    copylist.sort()

    if len(copylist) % 2 == 0:   # even length
        rightmid = len(copylist) // 2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid]) / 2.0
    else:
        mid = len(copylist) // 2
        median = copylist[mid]

    return median



def mean(alist):
    '''
    (list) -> float

    Given a list of values, the function computes a total which is then
    divided by the number of items, or the average of the list.

    Example:
    >>> mean([20, 32, 21, 26, 33, 22, 18])
    24.571428571428573
    '''

    mean = sum(alist) / len(alist)

    return mean


def mode(alist):
    '''
    (list) -> int

    Returns the count of each occurrence of the data items.

    Examples:
    >>> mode([1, 1, 4, 5, 6, 2, 4, 7, 1, 4, 6, 1])
    [1]
    >>> mode([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6])
    [4, 5]
    >>> mode([20, 32, 21, 26, 33, 22, 18])
    [20, 32, 21, 26, 33, 22, 18]
    '''

    countdict = genFrequencyTable(alist)

    countlist = countdict.values()
    maxcount = max(countlist)
    modelist = []

    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)

    return modelist



def genFrequencyTable(alist):
    '''
    (list) -> dictionary

    Given a list of numbers, the function generates a dictionary in which
    the key, or the number, and value, the frequency is added to.

    Returns coundict
    '''

    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1
            
    return countdict



def frequencyTable(alist):
    '''
    (list) -> list

    Displays a frequency distribution with a two-column table by using
    the dictionary that is created by 'genFrequencyTable'.
        1) First column - gives the data item
        2) Second column - gives the associated count
    '''

    countdict = genFrequencyTable(alist)

    itemlist = list(countdict.keys())
    itemlist.sort(reverse = True)

    print("ITEM", "FREQUENCY")

    for item in itemlist:
        # 7 spaces
        print(item, '{:>7}'.format(countdict[item]))

    return None




# EXTRA CREDIT

def frequencyChart(alist):
    '''

    '''

    # Call 'genFrequencyTable' to create dictionary
    countdict = genFrequencyTable(alist)

    itemlist = list(countdict.keys())
    minitem = 0
    maxitem = len(itemlist) - 1

    countlist = countdict.values()
    maxcount = max(countlist)

    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1, -1, maxitem + 1, maxcount + 1)
    chartT.hideturtle()

    chartT.up()
    chartT.goto(0, 0)
    chartT.down()
    chartT.goto(maxitem, 0)
    chartT.up()

    chartT.goto(-1, 0)
    chartT.write('0', font = ('Helvetica', 16, 'bold'))
    chartT.goto(-1, maxcount)
    chartT.write(str(maxcount), font = ('Helvetica', 16, 'bold'))
    
    for index in range(len(itemlist)):
        chartT.goto(index,-1)
        chartT.write(str(itemlist[index]),font=('Helvetica',13,'bold'))

        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index,countdict[itemlist[index]])
        chartT.up()

    wn.exitonclick()

    return None

# EXTRA CREDIT




def main():
    '''
    () -> None

    Uses a list of earthquake data,
        - Magnitudes of earthquakes that occured in one place over a
            number of years.
            
    Implements list into functions:
        - mean
        - median
        - mode
        - frequencyTable
        - frequencyChart
    '''

    equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
            2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
            4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
            4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
            2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
            4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
            3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
            2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
            2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
            6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
            2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
            2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
            4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
            4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
            2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
            2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
            2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
            4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
            4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
            2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
            3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
            2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
            2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
            2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
            2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
            2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
            3.1, 4.6, 2.8, 3.1, 6.3]

    table = frequencyTable(equakes)
    mean_li = mean(equakes)
    median_li = median(equakes)
    mode_li = mode(equakes)
    chart = frequencyChart(equakes)

    print(table, 'Mean: ', mean_li, '\nMedian: ', median_li, '\nMode: ',
          mode_li, '\n', chart)

    return None



print(doctest.testmod())


if __name__ == '__main__':
    main()
              


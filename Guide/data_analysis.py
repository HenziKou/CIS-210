'''
Data analysis. Project 6. Part 2
Author: Quinn Milionis
Credits: Bradley N. Mililer and David L. Ranum
Does basic data analysis on a list of numbers,
genFrequencyTable generates a histogram of the
frequeny of the values
'''

import turtle
import doctest
def median (alist):
    """
list -> float/int
given alist, returns the median value
of that list.
returns median
>>> median([1,3,5,7])
4.0
>>> median([1,4,5,7,9])
5
"""
    copylist = alist[:]
    copylist.sort()
    if len (copylist)%2 == 0:
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        median = copylist[leftmid] + copylist [rightmid]/2
    else:
        mid = len (copylist)//2
        median = copylist [mid]
    return median

def genFrequencyTable(alist):
    """
list -> dictionary
Given alist, generates a dictionay in
which the key is the number and the value
is the frequency of that number
returns countdict
"""

    countdict = {}
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
             countdict[item] = 1
    return countdict


def frequencyTable(alist):
    """
list -> None
Uses the dictionary created by
genFrequencyTable to sort and generate
a table of item frequency based on alist.
returns None
"""
    countdict = genFrequencyTable(alist)

    itemlist = list(countdict.keys())
    itemlist.sort()

    print('ITEM', 'FREQUENCY')

    for item in itemlist:
        print (item, '    ', countdict[item])
    return None

def frequencyChart(alist):
    """
list -> None
using the dictionary created by
genFrequencyTable, generates a
histogram based on the frequency
of values in alist using turtle graphics.
returns None
"""
    countdict = genFrequencyTable(alist)

    itemlist = list(countdict.keys())
    minitem = 0
    maxitem = len(itemlist)-1

    countlist = countdict.values()
    maxcount = max(countlist)

    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1,-1,maxitem+1,maxcount+1)
    chartT.hideturtle()

    chartT.up()
    chartT.goto(0,0)
    chartT.down()
    chartT.goto(maxitem,0)
    chartT.up()

    chartT.goto(-1,0)
    chartT.write('0',font=('Helvetica',16,'bold'))
    chartT.goto(-1,maxcount)
    chartT.write (str(maxcount), font=('Helvetica',16,'bold'))

    for index in range(len(itemlist)):
        chartT.goto(index,-1)
        chartT.write(str(itemlist[index]),font=('Helvetica',13,'bold'))

        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index,countdict[itemlist[index]])
        chartT.up()
    wn.exitonclick()

    return None
    

doctest.testmod()



##def mode(alist):
##    countdict = {}
##
##    for item in alist:
##        if item in countdict:
##            countdict[item] = countdict[item] + 1
##        else:
##            countdict[item] = 1
##
##    countlist = countdict.values()
##    maxcount = max(countlist)
##
##    modelist = []
##    for item in countdict:
##        if countdict[item] == maxcount:
##            modlist.append(item)
##
##    return modelist


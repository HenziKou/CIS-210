'''
Project 8 Parts 1 and 2
Author: Quinn Milionis
Credits: Bradley N. Mililer and David L. Ranum
A program that determines the major with the most
students in CIS 210 Winter Term 2016.
'''
#data_analysis_more.py

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

def mean(alist):
    """
list -> float
given alist, returns the mean of the numbers
in the list.
returns mean

>>> mean([1,2,3,4)]
2.5
"""
    mean = sum(alist) / len(alist)
    return mean


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



def mode(alist):
    """
list -> list
given alist, generates a list of the
mode of that given list
returns modellist
>>> mode(([1,2,3,2,5])
['2']
"""
    countdict = genFrequencyTable(alist)

    countlist = countdict.values()
    maxcount = max(countlist)

    modelist = []
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    
    return modelist

def majorsf_to_li(majorsf):
    """
creates a list of values in majorsf,
stripping the newline character and ignorning
the one occurance of "Major"
"""

    majorList = []
    for line in majorsf:
        line = line.strip()
        if line != 'Major':
            majorList.append(line)
    return majorList
        
def report(alist):
    """
list -> None
Calls the function mode, prints the most
represnted major, and then calls frequencyTable
which gerates a table to report the number of students
in each Major.
returns None
"""

    liMode = mode(alist)
    print('Most represented major(s):','\n',liMode[0],'\n')

    frequencyTable(alist)
    
    
def majors_main():
    """
() -> None
    Calls: majorsf_to_li, report

    top level function for analysis of data in file of
    majors of studnets in CIS 210 W16.

    Access major file, create list of relevant data,
    and report the mode and frequency table for the data
    in the filie.
    Returns None

>>> majors_main()
"""
    with open('majors_CIS210_W16.txt', 'r') as majorsf:
        majorsli = majorsf_to_li(majorsf)

    report(majorsli)

    return None
        

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

    print('{: <6} {: <9}'.format('ITEM', 'FREQUENCY'))

    for item in itemlist:
        
        print ('{: <6} {: <9}'.format(item, countdict[item]))
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


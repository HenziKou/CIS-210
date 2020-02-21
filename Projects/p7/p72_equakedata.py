'''
Project 7.2: Earthquake Watch
CIS 210

Author: Henzi Kou
Credits: N/A

Use file processing and data analysis to find and report information about
earthquake activity centered in Eugene, Oregon, over the past 100 years.

Practice with:
    - Data analysis
    - File processing
'''

import doctest

import p62_data_analysis as p62


def equake_readf(fname):
    '''
    (string) -> list

    Opens a file, 'fname', then creates and returns a list of the
    earthquake magnitudes from the file.
    '''

    fname.readline()
    maglist = []

    for line in fname:
        values = line.strip().split(',')
        maglist.append(float(values[4]))

    # EXTRA CREDIT
    maglist.sort()

    return maglist


def equake_analysis(magnitudes):
    '''
    (list) -> tuple

    Using the list 'magnitudes' created from 'equake_readf', the function will
    call functions from the data analysis file to determine the mean, median,
    and mode of the data in the 'magnitudes' list. The result is returned as
    a tuple.

    Example:
    >>> equake_analysis([3.0, 2.5, 6.0, 2.2, 2.5])
    (3.2399999999999998, 2.5, [2.5])
    '''

    li_mean = p62.mean(magnitudes)
    li_median = p62.median(magnitudes)
    li_mode = p62.mode(magnitudes)

    return li_mean, li_median, li_mode


def equake_report(mmm, magnitudes):
    '''
    (tuple, list) -> None

    Reports the number (count) of earthquakes, and the mean, median, and mode
    of 'magnitudes'. It will also call 'frequencyTable' to report the
    number of occurences of each item in 'magnitudes'.

    Example:
    >>> equake_report((3.2399999999999998, 2.5, [2.5]), [3.0, 2.5, 6.0, 2.2, 2.5])
    <BLANKLINE>
    	Earthquake Data Analysis 
    	100 Years Ago to Present
    	250km centered at Eugene, OR 
    <BLANKLINE>
    There have been 5 earthquakes over the past 100 years.
    <BLANKLINE>
    Mean magnitude is:  3.2399999999999998
    Median magnitude is:  2.5
    Mode(s) of magnitude is:  [2.5] 
    <BLANKLINE>
    ITEM FREQUENCY
    6.0       1
    3.0       1
    2.5       2
    2.2       1
    None
    '''

    count = len(magnitudes)
    
    print('\n\tEarthquake Data Analysis \n\t100 Years Ago to Present'
          '\n\t250km centered at Eugene, OR \n'
          '\nThere have been', count, 'earthquakes over the past 100 years.')

    print('\nMean magnitude is: ', mmm[0])
    print('Median magnitude is: ', (mmm[1]))
    print('Mode(s) of magnitude is: ', (mmm[2]), '\n')

    # EXTRA CREDIT
    print(p62.frequencyTable(magnitudes))
    
    return None


def main():
    '''
    () -> None

    Top level function for earthquake data analysis.
    
    Calls:
        - equake_readf
        - equake_analyis
        - equake_report

    Returns None.
    '''
    
    #fname = 'equake50f.txt'
    fname = open('equake25f.txt', 'r')
    #fname = 'test_data.txt'

    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(mmm, emags)

    return None


print(doctest.testmod())


if __name__ == '__main__':
    main()
    



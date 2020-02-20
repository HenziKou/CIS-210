'''
Project 7.1: Who is in this class?
    "Data Analysis"
CIS 210

Author: Henzi Kou
Credits: N/A

Use file processing and data analysis to find and report information about
the range of majors represented in CIS 210 in Fall 2017.

Practce with:
    - File processing and data analysis
'''

# Write 3 new functions: 'majors_readf, majors_analysis, majors_report'

import doctest

import p62_data_analysis as p62


def majors_readf(fname):
    '''
    (string) -> list

    Opens the file 'fname' and creates then returns a list of the majors
    in the file.
    '''

    fname.readline()
    majorsli = []

    for line in fname:
        line = line.strip().split()
        majorsli.append(line[0])

    return majorsli




def majors_analysis(majorsli):
    '''
    (list) -> int

    Will call function 'mode' from the data analysis module to determine
    the most frequently occurring item(s) (majors) in the argument
    list, and then return this result.

    Example:
    >>> majors_analysis(['CIS', 'EC', 'PS', 'GSS', 'PBA', 'CIS', 'CIS'])
    ['CIS']
    '''

    majors_mode = p62.mode(majorsli)

    return majors_mode


def majors_report(majors_mode, majorsli):
    '''
    (int, list) -> None

    By using the value returned by 'major_analysis' and 'majorsf', it will
    report the mode of 'majorsli' and will also call 'frequencyTable'
    to report the number of occurences of each item in 'majorsli'.

    >>> majors_report(['CIS'], ['CIS', 'EC', 'PS', 'GSS', 'PBA', 'CIS', 'CIS'])
    Most represented major(s): 
    CIS 
    <BLANKLINE>
    ITEM FREQUENCY
    PS       1
    PBA       1
    GSS       1
    EC       1
    CIS       3
    None
    '''

    print('Most represented major(s): ')
    print(majors_mode[0], '\n')
    # DOES NOT ALIGN PROPERLY - FIX IF POSSIBLE
    print(p62.frequencyTable(majorsli))
    
    return None



def main():
    '''
    () -> None
    
    Calls:
        - majors_readf
        - majors_analysis
        - majors_report
    
    Top level function for analysis of CIS 210 majors data.
    Returns None.
    '''
    
    fname = open('majors_cis210f17.txt', 'r')

    majorsli = majors_readf(fname)
    majors_mode = majors_analysis(majorsli)
    majors_report(majors_mode, majorsli)

    return None


print(doctest.testmod(), '\n')

# NOT RUNNING RIGHT OFF THE START - MUST FIX
if __name__ == '__main__':
    main()

    


# EXTRA CREDIT
'''
Write a new version of 'test_reverse' function from 'p61_testfunc.py' to test
the string reverse functions using test cases from file 'test_reverse.txt'.
Each line of this file should be correspond to one tuple from the test_cases
table, i.e., will have an example argument (test) and the expected result.
Note that you will need to use a separator other than space or comma, if you
want to test strings that contain either of those characters.
'''

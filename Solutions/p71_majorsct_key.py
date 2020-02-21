"""
CIS210 Project 7-1 Fall 2017 

Author: [Solution]

Credits: N/A

Read and report on data from file
of majors of students in CIS 210.

Practice:
-- basic file processing
-- data analysis
"""

import p62_data_analysis as da
import doctest

def majors_readf(fname):
    '''(str) -> list

    Return list of majors given in
    file of majors (fname).

    For example,
    
    >>> majors_readf('majors_short.txt')
    ['CIS', 'CIS', 'UNDL', 'COLT']
    '''
    with open(fname, 'r') as majorsf:
        majorsf.readline()  # move past title
        majorsli = []       # initialize majorsli
    
        for item in majorsf:
            item = item.rstrip().split()
            majorsli.append(item[0])
        
    return majorsli

def majors_analysis(majorsli):
    
    '''(list of CIS 210 info) -> list

    Calls: mode (from data analysis module)

    Determine the mode in a list of
    CIS 210 majors data; return mode.

    Calls: mode (from imported module)

    >>> majors_analysis(['CIS', 'CIS', 'ECON', 'PSY', 'UNDL', 'UNDL'])
    ['CIS', 'UNDL']
    '''
    eqMode = da.mode(majorsli)

    return eqMode

def majors_report(majors_mode, majorsli):
    '''(list of strings) -> None

    Calls: freqTable
    (from data analysis module)

    Reports the mode of the majorsli; and
    generates a frequency table for majorsli
    and reports this.

    >>> majors_report(['CIS'], ['CIS', 'CIS', 'UNDL', 'COLT'])
    Most represented major(s):
    CIS

    ITEM   FREQUENCY
    CIS    2               
    COLT   1               
    UNDL   1        
    '''
    print('Most represented major(s):')
    for item in majors_mode:
        print(item)
    print()

    da.frequencyTable(majorsli)
    #da.freqChart(majorsli)

    return None
        
def main():
    '''() -> None

    Calls:  majorsf_to_li, report

    Top level function for analysis of
    data in file of majors of students
    in CIS 210 F17.

    File format:  one line header followed
    by multiple lines of <major> <college>, e.g.,
    CIS CAS

    Open and close the file, create list
    of relevant data, and report the mode
    and frequency table for the data.

    Returns None.

    >>> main()
    '''
    #fname = 'p71exampledata.txt'
    fname = 'majors_cis210f17.txt'
        
    majorsli = majors_readf(fname)          #read
    majors_mode = majors_analysis(majorsli) #analyze
    majors_report(majors_mode, majorsli)    #report

    return None


if __name__ == '__main__':
    main()




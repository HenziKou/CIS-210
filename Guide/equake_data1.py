'''
Project 9 part 1
Author: Quinn Milionis
Credits: Bradley N. Mililer and David L. Ranum
performs data analysis on earthquake data pulled
from the internet.
'''




import data_analysis_more as d
import urllib.request

url = 'http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=1916-02-01&latitude=44.0519&longitude=-123.0867&maxradiuskm=250&minmagnitude=5'


def readqf():
    """
str -> list
opens earthquake data from USGS website and stores
the magnitudes in magList
Returns magList

>>>readqf()
"""
    magList = []
    with urllib.request.urlopen(url) as webpage:
        firstLine = 1
        for line in webpage:
            if firstLine != 1:
                line = line.decode('utf-8')
                line = line.strip()
                line = line.split(',')
                magList.append(float(line[4]))
                #print (line)
            firstLine = 0
    #print (magList)
    return magList

def equake_analysis(mags):
    """
list -> none
calls functions mean, median, and mode
to analyze the earthquake magnitude data
and report the results. also calls
frequencyTable.
>>> equake_analysis(mags)
 Mean:  5.37 
 Median:  8.0 
 Mode:  [5.4, 5.2] 

ITEM   FREQUENCY
5.0    1        
5.1    1        
5.2    1        
5.3    1        
5.4    1        
5.6    1        
5.7    1        
5.8    1 
"""
    mean1 = d.mean(mags)
    median1 = d.median(mags)
    mode1 = d.mode(mags)
    print (' Mean: ',mean1,'\n','Median: ',median1,'\n','Mode: ',mode1,'\n')
    d.frequencyTable(d.genFrequencyTable(mags))
    return None

def equake_main():
    """ () -> None

Calls: readeqf, equake_analysis

top level function for analysis of earthquake
data from USGS website.

Returns None.

 Mean:  5.37 
 Median:  8.0 
 Mode:  [5.4, 5.2] 

ITEM   FREQUENCY
5.0    1        
5.1    1        
5.2    1        
5.3    1        
5.4    1        
5.6    1        
5.7    1        
5.8    1 
>>> equake_main()
"""
    emags = readqf()
    equake_analysis(emags)

    return None


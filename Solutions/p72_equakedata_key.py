'''
CIS210 Project 7 Part 2 CIS 210 Fall 2017

Author: [Solution]

Credits: N/A

Use data analysis functions from project 6-2
to analyze and report on earthquake data.

Practice:
-- file processing
-- data analysis

Data from
# http://earthquake.usgs.gov/fdsnws/event/1/
'''
import doctest
import p62_data_analysis as da

def equake_readf(fname):
   '''(str) -> list

   Return list of earthquake magnitudes
   from file of earthquake information.

   For example,
    
   >>> equake_readf('equakes_short.txt')
   [5.2, 5.1]  
   '''
   with open(fname, 'r') as eqf:    
      mags = []
      eqf.readline()    #move past header
      for line in eqf:
         vals = line.strip().split(',')
         mag = float(vals[4])
         mags.append(mag)

      #print(len(mags))

   return mags

def equake_analysis(magnitudes):
   '''(list of floats-equake magnitudes) -> None

   Analyze data in input list of earthquakes
   magnitudes and report on it.
   None value is returned.

   Calls: mean, median, mode, (standardDev,)
   (from p62)

   >>> equake_analysis([2.5, 3.1, 2.8, 2.8])
   (2.8, 2.8, [2.8])
   '''
   eqMean = da.mean(magnitudes)
   eqMedian = da.median(magnitudes)
   eqMode = da.mode(magnitudes)
   #eqStdDev = da.standardDev(mags)

   return (eqMean, eqMedian, eqMode)

def equake_report(magnitudes, mmm, chart=False):
   '''(list, tuple, Boolean) -> None

   Report results of data analysis
   for list of equake magnitudes (mags):
   mean, median, and mode (mmm).
   If chart, then draw a table, too.
   Return None.

   calls:  freqChart, drawTable (from module)

   >>> equake_report([2.5, 3.1, 2.8, 2.8],
                    (2.8, 2.8, [2.8]))
   <report and chart>
   '''
   eqMean, eqMedian, eqMode = mmm

   titlew = 40
   print('Earthquake Data Analysis'.center(titlew))
   print('100 Years Ago to Present'.center(titlew))
   print('250km centered at Eugene, OR'.center(titlew))
   print()
   print('There have been {} earthquakes over the past 100 years.'.format(len(magnitudes)))
   print()
   print('Mean magnitude is: {:2f}'.format(eqMean))
   print('Median magnitude is: {}'.format(eqMedian))
   print('Mode(s) of magnitudes is: {}'.format(eqMode))
   #print('Standard deviation is: {:2f}'.format(eqStdDev))
   print()

   da.frequencyTable(magnitudes)
   if chart:
      da.freqChart(magnitudes)
   
   return None

def main():
   '''() -> None

   Retrieve, analyze, and report on
   earthquake data centered in
   Eugene, OR for past 100 years.

   equakes.txt (13 lines) is magnitude 5 earthquakes
   equakes_short.txt is first 2 line of equakes.txt
   equakes_long.txt (3097 lines) is magnitude 2.5 earthquakes

   Calls:  readeqf, equake_analysis, equake_report

   >>> main()
   '''
   fname = 'equakes50f.txt'
   #fname = 'equakes25f.txt'
   #fname = 'equakes_short.txt'
   
   emags = equake_readf(fname)
   mmm = equake_analysis(emags)
   equake_report(emags, mmm)
   #equake_report(emags, mmm, True)

   return None

'''
if __name__ == '__main__':
   main()
'''   
   


 

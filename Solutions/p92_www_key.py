'''
CIS210 Project 9-1b Fall 2017

Use USGS API to access earthquake data at the website.
Create a data dictionary.

Author: [Solution]

Credits: N/A

Practice:
-- file processing with internet and API
'''
import urllib.request
import p8_equakes_vis_key as p8

#auxiliary function to count lines in a file
def flinesCtr(f):
   ''' count and return number of lines in file'''

   with open(f) as ctf:
      for i, l in enumerate(ctf):
            pass
   num_lines = i + 1
   '''
   num_lines = sum(1 for line in open(fname))
   '''
   return num_lines

#####
# get earthquake data from USGS website and
# store longitude, latitude information in a
# data dictionary that can be used by Project 8
# when used, replaces call to readFile
# in visualizeQuakes, i.e.,
# eqDict = readeqdd()
#####
def readeqdd():
   '''() -> dictionary of equake longitudes, latitudes

   Use USGS API to get data about earthquake
   events of magnitude >= 5 around the world
   for the past year;
   store earthquake longitude and latitudes
   in a dictionary, which is returned.
   (See comment at the end of this module for
   structure of one line of data.)

   Called by: visualizeQuakes (and clusterAnalysis)

   For example,
   >>> readeqdd()
   {1: [-122.75, 45.68], 2: [-121.73, 43.53]} 
   '''
   with urllib.request.urlopen(
'http://earthquake.usgs.gov/fdsnws/event/1/\
query?format=csv\
&starttime=2016-11-01\
&minmagnitude=5') as eqf:
      
      eqdict = {}
      key = 0
      eqf.readline() # move past header
      for line in eqf:
         line = line.decode()
         line = line.strip().split(',')
         latitude = round(float(line[1]), 2)
         longitude = round(float(line[2]), 2)
         key += 1
         eqdict[key] = (longitude, latitude)

   #(len(eqdict))
   return eqdict

def visualizeQuakes(k, r):
   '''(int, int) -> None

   Computes and reports a k-means cluster analysis
   for data access by readeqdd (at USGS website).
   Stops after r iterations of the createClusters
   function.
   
   Uses turtle graphics to plot the clusters
   on a world map.
   
   Returns None.

   Calls:  readeqdd, createCentroids, createClusters, eqDraw

   For example,
   >>> visualizeQuakes(3, 5, 'earthquakes.csv')
   >>> visualizeQuakes(5, 10, 'earthquakes.txt')
   <results plotted as points on world map>
   '''
   '''
   test data dictionary
   eqDict = {0:[34], 1:[44], 2:[10], 3:[99],
             4:[50], 5:[67], 6:[0], 7:[28],
             8:[50], 9:[100]}
   '''   
   eqDict = readeqdd()                          #access file (create dd)
   eqCentroids = p8.createCentroids(k, eqDict)  #analyze data (data mining)
   eqClusters = p8.createClusters(k, eqCentroids,  #more analyze data
                                eqDict, r)
   p8.eqDraw(k, eqDict, eqClusters)             #report results of data analysis
   
   return None

def main():
   '''controller for earthquake data processing'''
   k = 6
   r = 10
   visualizeQuakes(k, r)
   return None

if __name__ == '__main__':
   main()


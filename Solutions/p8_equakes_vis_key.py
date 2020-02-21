'''
CIS210 Project 8 Final Project Fall 2017

Earthquake data here is for earthquakes around the world over the
past year (since 11-01-16) magnitude 5 or higher
(1753 lines of data 11-14-17).

Author: [Solution]

Credits: N/A

Access file of earthquake data (> 5.0 magnitude over past year);
implement k-means cluster analysis algorithm to analyze the data;
use turtle graphics to plot the results on a world map.

Functions to read and process the earthquake
data are adapted from the text and project 9-1.

Functions euclidD, createCentroids, and
createClusters are all copied from text. Ch. 7.

visualizeQuakes is based on the function in
Ch. 7 of the text. visualizeQuakes here
has k and r as parameters, as well as the
dataFile parameter. Also visualizeQuakes
calls function eqDraw to draw the equake data.
(visualizeQuakes is now like clusterAnalysis
from the text, with revised parms and with
the addition of a call to eqDraw.)

eqDraw is a new function called by
visualizeQuakes to do the work of drawing
the results of the k-means analysis on a world map.

Practice:
-- k-means cluster analysis
-- program with multiple functions; implement, revise, document code
'''
import doctest
import math
import random
from turtle import *

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
# function to access file of earthquake data.
#####

#####
# .txt file of earthquake data --> data dictionary
# with information about longitude and latitude
# of each quake
# dd format: {1:[<long>, <lat>], 2:[<long>, <lat>]}
#####
def readFile(f):
   '''(str) -> dict

   Create and return a dictionary
   of the long/lat data in file f.  This
   data was previously accessed from the USGS
   USGS website and stored in a .csv file.

   >>> createdd('equakes.csv')
  
   '''
   with open(f, 'r') as eqf:
      eqdict = {}

      key = 0
      eqf.readline() #move past header (if there is one)
      for line in eqf:
         line = line.strip().split(',')
         latitude = float(line[1])
         longitude = float(line[2])
         key += 1
         eqdict[key] = [longitude, latitude]

      #print(eqdict)

   return eqdict

# function called by clusterAnalysis
# for testing k-means cluster analysis
# functions during project development

#f = 'scores.txt'
def createdd_test(f):
   '''(str) -> dict

   Create and return a dictionary
   of the data in file f (one score
   per file line)

   Called by: clusterAnalysis (in testing phase)

   >>> createdd_test('scores.txt')
   {1: [89], 2: [92]}
   '''
   with open(f, 'r') as dataf:
      datadict = {}

      key = 0
      for line in dataf:
         key += 1
         score = int(line.rstrip())

         datadict[key] = [score]

   return datadict

#####
# cluster analysis functions
#####

def euclidD(point1, point2):
   '''(list, list) -> number

   Computes and returns the
   Euclidean distance between
   point1 and point2 (which must
   have same dimensions).

   Called by: createClusters

   >>> euclidD((3,0), (0,4))
   5.0
   '''
   total = 0
   for index in range(len(point1)):
      diff = (point1[index] - point2[index]) ** 2
      total = total + diff

   euclidDistance = math.sqrt(total)
   return euclidDistance

#result, for example:  [[34], [45], [44]]
def createCentroids(k, datadict):
   '''(int, dictionary) -> list (of dict values)

   Create a starter list of k centroids
   for a k-cluster algorithm by
   randomly choosing from the items
   in datadict.  The starter list is returned.

   Called by: visualizeQuakes

   >>> createCentroids(1,{1: [2.77], 2: [2.97]})
   [[2.77]]
   '''
   centroids = []
   centroidCount = 0
   centroidKeys = []

   while centroidCount < k:
      rkey = random.randint(1, len(datadict))

      #keys cannot repeat
      if rkey not in centroidKeys:
         centroids.append(datadict[rkey])
         centroidKeys.append(rkey)
         centroidCount += 1

   #print(centroids)        
   return centroids

#####
# main cluster analysis function 
#####

def createClusters(k, centroids, datadict, repeats):
   '''(int, list of lists, dict, int) -> list of lists

   Does main work of k-means cluster analysis.
   Create list of k clusters of data from dict,
   and return this list.
   
   The clusters are formed around k cluster centroid
   points.  The centroid points are re-calculated
   repeats times, after each iteration of cluster
   creation.

   Called by: visualizeQuakes
   Calls:  euclidD

   For example,
   >>> createClusters(3, [[2.77], [4], [5.2]],
   {1:[2], 2:[2.77], 3:[3.3], 4:[4], 5:[5.2], 6:[5.4]},
   5)
   [[1, 2, 3], [4], [5, 6]]
   >>> createClusters(3, [[2.77], [4], [5.2]],
   {1:[2], 2:[2.77], 3:[3.3], 4:[4], 5:[5.2], 6:[5.4],
   7:[4.4], 8:[2.1], 9:[3.4], 10:[5.1]},
   5)
   [[1, 2, 8], [3, 4, 7, 9], [5, 6, 10]]
   '''
   for i in range(repeats):
      #print('PASS:', i)

      # create initial list of k empty clusters
      clusters = []
      for j in range(k):
         clusters.append([])

      # assign each item in data dictionary
      # to its proper cluster (one where item
      # is least distant from the centroid)
      for akey in datadict:
         distances = []

         # compute the distance between the
         # data point and each centroid
         for centroidsIndex in range(k):
            dist = euclidD(datadict[akey],
                           centroids[centroidsIndex])
            distances.append(dist)

         # check for minimum distance and
         # store item key in appropriate cluster
         mindist = min(distances)
         index = distances.index(mindist)

         clusters[index].append(akey)
         
      # after a round of creating clusters,
      # recompute the centroids for each cluster
      dimensions = len(datadict[1])
      for clusterIndex in range(k):
         sums = [0] * dimensions
         for akey in clusters[clusterIndex]:
            datapoints = datadict[akey]
            for i in range(len(datapoints)):
               sums[i] += datapoints[i]

         for i in range(len(sums)):
            clusterLen = len(clusters[clusterIndex])
            if clusterLen != 0:
               sums[i] = sums[i] / clusterLen

         centroids[clusterIndex] = sums
      '''
      # report clusters after each pass (small files only)
      for i in range(len(clusters)):
         print('CLUSTER', i, end=' ')
         for key in clusters[i]:
            print(datadict[key], end=' ')
         print()

      print('CENTROIDS:', centroids)
      print()
      '''
   return clusters

#####
# report results of
# k-means analysis
# on world map
#####

def eqDraw(k, eqDict, eqClusters):
   '''(int, dict, list) -> None

   Uses data from the earthquake dictionary
   eqDict and cluster analysis eqClusters
   to draw earthquake clusters on a world map.
   Returns None.

   Called by: visualizeQuakes

   '''
   speed('fastest')
   bgpic('worldmap1800_900.gif')
   screensize(1800, 900)
   
   wFact = (screensize()[0]/2) / 180
   hFact = (screensize()[1]/2) / 90

   hideturtle()
   penup()

   # note: len colorlist should match k
   colorlist = ['red', 'green', 'blue',
                'orange', 'yellow', 'purple']
 
   for clusterIndex in range(k):
      color(colorlist[clusterIndex])
      for akey in eqClusters[clusterIndex]:
         longitude = eqDict[akey][0]
         latitude = eqDict[akey][1]
         goto(longitude*wFact, latitude*hFact)
         dot(5)

   #exitonclick()

   return None
              
def visualizeQuakes(k, r, f):
   '''(int, int, str) -> None

   Computes and reports a k-means cluster analysis
   for data in file f.
   Stops after r iterations of the createClusters
   function.
   
   Uses turtle graphics to plot the clusters
   on a world map.
   
   Returns None.

   Calls:  readeqf, createCentroids, createClusters, eqDraw

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
   eqDict = readFile(f)                      #access file (create dd)
   #print(len(eqDict))
   
   eqCentroids = createCentroids(k, eqDict)  #analyze data (data mining)
   
   eqClusters = createClusters(k, eqCentroids,  #more analyze data
                                eqDict, r)
   
   eqDraw(k, eqDict, eqClusters)             #report results of data analysis
   
   return None

def main():
   '''controller for earthquake data processing'''
   k = 6
   r = 10
   #f = input('file? ')
   f = 'earthquakes.txt'
   #f = 'earthquakes_short.txt'
   #print(flinesCtr(f))           #will be 1 more than dd due to header
   visualizeQuakes(k, r, f)
   return None


if __name__ == '__main__':
   main() 

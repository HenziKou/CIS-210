'''
Project 8-f (Final Project): World-Wide Earthquake Watch
CIS 210

Author: Henzi Kou
Credits: N/A

Use file processing and data mining to discover patterns of earthquake
activity around the world over the past year; plot results on a world map.

Practice with:
    - Data mining and file processing
    - Reading, understanding, and revising a program that has mostly been
        already written. Requires a thorough understanding of the 'k-means
        cluster analysis' algorithm and file processing.
'''


# LOOK AT THIS WEEK'S CLASS NOTES

import math
import doctest
from turtle import *
import random

# Create 'readFile' function from Chapter 7
def readFile(filename):
    '''
    (string) -> dictionary

    Given a file, the function analyzes and returns a dictionary of
    earthquake data.

    Example:
    >>> readFile('test_data.txt')
    {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576]}
    '''

    with open(filename, 'r') as datafile:
        datadict = {}
        key = 0
        datafile.readline()
        
        for line in datafile:
            line = line.strip().split(',')
            lat = float(line[1])
            lon = float(line[2])
            key += 1
            datadict[key] = [lon, lat]

    return datadict



# Create 'euclidD' function from Chapter 7
# ADD DOCSTRINGS AND IN-LINE COMMENTS
def euclidD(point1, point2):
    '''
    (list, list) -> number

    Computes the distance between two points using the Euclidean distance
    algorithm. Each point is defined as a list of n coordinate values.

    Example:
    >>> euclidD([1, 2, 3, 4], [10, 9, 8, 7])
    12.806248474865697
    >>> euclidD([36.0645,129.2695], [-17.4576,-174.6136])
    308.5604538077101
    '''

    sum = 0

    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        sum = sum + diff

    euclidDistance = math.sqrt(sum)

    return euclidDistance
# DONE




# Create 'createCentroids' function from Chapter 7
# ADD DOCSTRINGS AND IN-LINE COMMENTS
def createCentroids(k, datadict):
    '''
    (number, dictionary) -> list

    Creates an empty 'centroid' list. The process continues until 'k'
    centroids have been selected.
    '''

    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = random.randint(1, len(datadict))

        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return centroids





# Create 'createClusters' function from Chapter 7
# ADD DOCSTRINGS AND IN-LINE COMMENTS
def createClusters(k, centroids, datadict, repeats):
    '''
    (number, list, dictionary, number) -> list

    Return a list of the clusters. Each cluster will be represented by a list.
    '''

    for apass in range(repeats):
        #print("****PASS", apass, "****")
        clusters = []

        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []

            for clusterIndex in range(k):
                dist = euclidD(datadict[akey], centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])

        for clusterIndex in range(k):
            sums = [0] * dimensions

            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]

                for ind in range(len(datapoints)):
                    sums[ind] += datapoints[ind]

            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind] / clusterLen

            centroids[clusterIndex] = sums

        #for c in clusters:
            #print('CLUSTERS')

            #for key in c:
                #print(datadict[key], end = ' ')
            #print()

    return clusters




# Create 'eqDraw' function
def eqDraw(k, eqDict, eqClusters):
    '''
    (number, dictionary, list) -> None

    Plots the earthquake data on a world map.
    '''

    speed('fastest')
    bgpic('worldmap1800_900.gif')
    screensize(1800, 900)

    wFact = (screensize()[0] / 2) / 180
    hFact = (screensize()[1] / 2) / 90
    
    hideturtle()
    penup()

    colorlist = ['red', 'green', 'blue', 'orange', 'cyan', 'yellow']

    for clusterIndex in range(k):
        color(colorlist[clusterIndex])

        for akey in eqClusters[clusterIndex]:
            lon = eqDict[akey][0]
            lat = eqDict[akey][1]
            goto(lon * wFact, lat * hFact)
            dot(5)

    return None

    


# Create 'visualizeQuakes' function from Chapter 7
def visualizeQuakes(k, r, dataFile):
    '''
    (number, number, string) -> None

    Calls the functions:
        - readFile
        - createCentroids
        - createClusters
        - eqDraw
    Then maps out the longitude and latitude points on a world map.
    '''

    datadict = readFile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)
    draw = eqDraw(k, datadict, clusters)

    return None





# Create 'main' function
def main():
    '''
    () -> None

    Top level function that calls:
        - visualizeQuakes
    '''

    f = 'earthquakes.txt'
    r = 10
    k = 6
    
    visualizeQuakes(k, r, f)

    return None



print(doctest.testmod())


if __name__ == '__main__':
    main()
    
    
    
    






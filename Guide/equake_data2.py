'''
Project 9 part 2
Author: Quinn Milionis
Credits: Bradley N. Mililer and David L. Ranum
A program that maps out earthquake locations
and color codes them based on cluster
'''



import random
import math
import urllib.request
import turtle
def euclidD (point1, point2):
    """
list, list -> float
given two points of any dimension, returns
the eclliduan distance between these ponits.
called in createClusters
returns euclidDistance
>>> euclidD([12,1],[39,21])
33.60059523282288
"""   
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff

    euclidDistance = math.sqrt(total)
    return euclidDistance



##def readFile(filename):
##    datafile = open(filename, 'r')
##    datadict = {}
##
##    key = 0
##    for aline in datafile:
##        key = key + 1
##        score = int(aline)
##
##        datadict[key] = [score]
##
##    return datadict
##
##def readFile(filename):
##    datafile = open(filename,'r')
##
##    datadict = {}
##
##    key = 0
##    aline = datafile.readline()
##    while aline != "":
##        key = key + 1
##        score = int(aline)
##        datadict[key] = [score]
##
##        aline = datafile.readline()
##
##    return datadict

url = 'http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2016-02-01&minmagnitude=5'
filename = 'query.csv'
def readeqf(url):
    """
str -> dictionary
given a url for earth quake data, pulls longitude and
latidute information and stores this in a dictionary.
Called by visualizequakes.
return datadict
"""
    with urllib.request.urlopen(url) as webpage:
        datadict = {}
        key = 0
        webpage.readline()
        for aline in webpage:
            aline = aline.decode('utf=8')
            items = aline.split(',')
            key = key + 1
            lat = float((items[1]))
            lon = float((items[2]))
            datadict[key] = [lon,lat]
        return datadict
        
        


def createCentroids(k, datadict):
    """
num, dictionary -> list
given number of centroids, k, and datadict,
generates centroids.
called by visualizeQuakes
returns centroids
"""
    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = random.randint(1,len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return centroids


def createClusters(k, centroids, datadict, repeats):
    """num, list, dictionary, num -> list
given k, number of cluster, a list of centorids, a dictionary
of data values, and number of repeates, generates the given
number of clusters.
called by visualizequakes
>>> createClusters(3, centroidList, dataDict, 3)
returns Clusters
"""
    for apass in range (repeats):
        #print("****PASS", apass, "****")
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey],centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range (k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/clusterLen

            centroids[clusterIndex] = sums

##        for c in clusters:
##            print ("CLUSTER")
##            for key in c:
##                print (datadict[key], end=" ")
##                print ()

    return clusters
                

def clusterAnalysis(datafile):
    
    dict = readFile(datafile)
    centroids = createCentroids(5,dict)
    clusters = createClusters(3,centroids,dict,2)
    
    
def visualizeQuakes(k,r):
    """
num, num -> none
calls readeqf, quakeCentroids, createClusters
given number of centroids and clusters to create and number of
repeats to the cluster creation, generates a visualization of
earthquakes on a world map, color coded to show cluster.
returns None
>>> visualizeQuakes(3,2)

"""
    datadict = readeqf(url)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)

    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic('worldmap.gif')
    quakeWin.screensize(1800,900)
    
    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()
    
    colorList = ['red', 'green', 'blue', 'orange', 'cyan', 'yellow']
    
    for clusterIndex in range (k):
        quakeT.color(colorList[clusterIndex])
        for akey in clusters[clusterIndex]:
            lon = datadict[akey][0]
            lat = datadict[akey][1]
            quakeT.goto(lon*wFactor,lat*hFactor)
            quakeT.dot()
    quakeWin.exitonclick()















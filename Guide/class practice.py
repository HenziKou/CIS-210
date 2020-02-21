

def readFile(filename):
    """
"""
    with open (filename,'r') as datafile:
        datadict = {}

        key = 0
        aline = datafile.readline()
        while aline != "":
            key = key + 1
            score = int(aline)
            datadict[key] = [score]

            aline = datafile.readline()

    return datadict

#print (readFile('score.txt'))

import random

def createCentroids(k, datadict):
    """
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

print (createCentroids(3,readFile('score.txt')))

def distance(a,b):
    """
list of int,list of int -> float
compute the euclidian distance
"""
    for i in range(len(a)):
        total += (a[i]-b[i]**2
    return sqrt(total)

def createClusters(r, centroids, datadict, r):
    """
"""
    clusters = [[], [], []] # This line is wrong if k not equal 3

    #on each pass (unitl r passes):
    for i in range(r):
        # resent cluster to empty
        clusters = [[], [], []]

        #for each key in datadict
        for key in datadict:

            #for each centroid
            for c in centroids:
                #compute distance betwen
                #datadict value and the centroid
                d = distance(c,datadict[key])

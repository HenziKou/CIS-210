'''
Project 9.2 - Data from the Web: Part 2
CIS 210

Author: Henzi Kou
Credits: N/A

Use Python modules to access data on the web.

Practice with:
    - Python urllib package; APIs.
'''


import urllib.request
import p8f_equakes_vis as p8


def readeqdd():
    '''
    () -> dictionary

    Accesses data from USGS about earthquake events of magnitude 5 or higher
    around the world, over the past year. Stores the information in a
    data dictionary.
    '''

    link = 'http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2016-11-01&minmagnitude=5'
    
    with urllib.request.urlopen(link) as eqf:
        data = {}
        key = 0
        eqf.readline()
        
        for line in eqf:
            line = line.decode().strip().split(',')
            #print(line)
            lat = float(line[1])
            lon = float(line[2])
            key += 1
            data[key] = [lon, lat]

    return data
        
        


def visualizeQuakes(k, r):
    '''
    (number, number, string) -> None

    Calls the functions:
        - readeqdd
        - createCentroids
        - createClusters
        - eqDraw
    Then maps out the longitude and latitude points on a world map.
    '''

    datadict = readeqdd()
    quakeCentroids = p8.createCentroids(k, datadict)
    clusters = p8.createClusters(k, quakeCentroids, datadict, r)
    draw = p8.eqDraw(k, datadict, clusters)

    return None



def main():
    '''
    () -> None

    Top level function that calls:
        - visualizeQuakes
    '''

    r = 10
    k = 6
    
    visualizeQuakes(k, r)

    return None


if __name__ == '__main__':
    main()



    

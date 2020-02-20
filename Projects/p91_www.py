'''
Project 9.1 - Data from the Web: Part 1
CIS 210

Author: Henzi Kou
Credits: N/A

Use Python modules to access data on the web.

Practice with:
    - Python urllib package; APIs
'''


import urllib.request
import p8f_equakes_vis as p8


def readeqf(fname):
    '''
    (string) -> file

    Given a url for data about earthquake events of magnitude 5 or higher,
    in the 250 km radius centered around Eugene, OR, over the past 100
    years, creates a file with the data.
    '''

    with urllib.request.urlopen(fname) as eqf:
        eqf.readline()

        for line in eqf:
            line = line.decode().strip().split(',')
            lat = line[1]
            lon = line[2]

            f = open('eugene_equakes.csv', 'w')
            f.write(str(lon))
            

        f.close
	
    return f



def main():
    '''
    () -> None
    
    Controller for earthquake data processing
    '''
    
    k = 6
    r = 10
    f = 'http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=1916-11-01&latitude=44.052071&longitude=-123.086754&maxradiuskm=250&minmagnitude=5'
    
    readeqf(f)
    vis = p8.visualizeQuakes(k, r)
    
    return None

'''
if __name__ == '__main__':
    main()
'''
    

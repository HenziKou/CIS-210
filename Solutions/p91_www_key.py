'''
CIS210 Project 9-1 Fall 2017

Use USGS API to access earthquake data at the website.
Create a file.

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
#function to access USGS website and create
#.csv file of the data returned by API query
#####

def readeqf(f):
   '''(string) -> None

   Use USGS API to get data about earthquake
   events centered in Eugene, OR, of magnitude
   5 or higher, over the past 100 years.

   >>> readeqf('eugene_equakes.csv')
   '''  
   with urllib.request.urlopen(
'http://earthquake.usgs.gov/fdsnws/event/1/\
query?format=csv\
&starttime=1916-11-01\
&latitude=44.052071\
&longitude=-123.086754\
&maxradiuskm=250\
&minmagnitude=5') as eqf:

      with open(f, 'w') as savef:      
         #eqf.readline() # move past header
         for line in eqf:
            print(line)
            line = line.decode('utf-8')
            savef.write(line)

   return None

def main():
   '''controller for earthquake data processing'''
   #f = 'testp91.csv'
   f = 'eugene_equakes.csv'
   readeqf(f)
   k = 3
   r = 10
   p8.visualizeQuakes(k, r, f)
   return None

'''
if __name__ == '__main__':
   main()
'''

'''
Alpha Pin Decode. Project 4 part 1 CIS 210
Author: Quinn Milionis
Credits: N/A
given an alphacode, converts the code back
into the pin.
'''



def alphapinDecode_stub (word):
    """
Str -> int
Given an alphacode, converts this alphacode back
into the  pin number.
Returns Pin
>>> alphapinDecode('lohi')
4327
"""
    pass
    #return pin

def alphapinDecode (word):
    """
Str -> str
Given a alphacode, converts this alphacode back
into the orgional pin number.
Returns Pin
>>> alphapinDecode('lohi')
4327
"""
    pin = ''
    vowelList = 'aeiou'
    consonantList = 'bcdfghjklmnpqrstvwyz'
    
    twoSplit = [word[i:i+2] for i in range(0, len(word), 2)]
    #print(twoSplit)
    for word in twoSplit:
        pin += str((consonantList.find(word[0]) * 5) + vowelList.find(word[1])) 
        
    #print(pin)
    return pin



alphapinDecode("lohi")
alphapinDecode("dizo")
alphapinDecode("begomari")
alphapinDecode("lililili")


        

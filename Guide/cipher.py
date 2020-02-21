#project 3 part 1
import random

'''
Substitution cipher. Project 3, Part 1. CIS 210
Author: Quinn Milionis
Credits: Bradley N. Mililer and David L. Ranum
Given text and a password, substitutionEncrypt
creates a cypher based off the given password.
SubstitutionDecript converts that cypher back
into readable plain text when given the same password.
'''

def removeDupes (myString):
    newStr = ''
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr

def removeMatches(myString,removeString):
    newStr = ''
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr

def genKeyFromPass (password):
    key = 'abcdefghijklmnopqrstuvwxyz'
    password = removeDupes (password)
    lastChar = password [-1]
    lastIdx = key.find (lastChar)
    afterString = removeMatches (key[lastIdx+1:],password)
    beforeString = removeMatches (key[:lastIdx],password)
    key = password + afterString + beforeString
    return key

def substitutionEncrypt (plainText, password):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherText = ''
    #removes spaces:
    plainText = plainText.replace(' ','')
    key = genKeyFromPass (password)
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
        #print (key)
    return cipherText

def substitutionDecrypt_stub (cipherText, password):
        """
string,string -> string
given the cipherText and the orginal password
used to create the cipherText, return the
orginal plain text.
>>> substitutionDecrypt ('qdznrexgjoltkblu', 'ajax')
'thequickbrownfox'
"""
        pass
    #return plainText

def substitutionDecrypt (cipherText, password):
    """
string,string -> string
given the cipherText and the orginal password
used to create the cipherText, return the
orginal plain text.
>>> substitutionDecrypt ('qdznrexgjoltkblu', 'ajax')
'thequickbrownfox'
"""
    plainText = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = genKeyFromPass (password)
    for ch in cipherText:
        idx = key.find(ch)
        #print (idx)
        plainText = plainText + alphabet[idx]
    return plainText






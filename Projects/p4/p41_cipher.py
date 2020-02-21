'''
Substitution Cipher
CIS 210

Author: Henzi Kou
Credits:

Using a susbstitution cipher algorithm to encrypt and decrypt a plain
text message.
    - Design a program with multiple functions such as:
        1. top-down design
        2. bottom-up code
        3. revising code
    - Doctest module for automated testing
    - Includes a main function to call on all other functions
'''

import doctest

def main():
    '''
    Calls the functions:
        - substitutionEncrypt(plainText, psw)
        - substitutionDecrypt(cipherText, psw)
        - genKeyFromPass(password)
    to execute the whole program.
    '''
    plainT = input("Type something.")
    psw = input("psw")
    
    p_Text = substitutionEncrypt(plainT, psw)
    # (1) Use built-in 'input' function to get a string to encrypt and password
    # (2) Call 'substitutionEncrypt' to encrypt the password
    print(p_Text) # <--- IS THIS CORRECT?

    
    # (4) Call 'substitutionDecrypt' to convert the value returned by
    #     'substitutionEncrypt' back to plaintext
    print(substitutionDecrypt(p_Text, psw)) # <--- IS THIS CORRECT?
    
    # (5) Print the value returned by 'substitutionDecrypt'
    return None


def substitutionEncrypt(plainText, psw):
    '''
    (str, str) -> str

    Given the alphabet the program will encript the string with a given
    password key.

    Example:
    >>> substitutionEncrypt('the quick brown fox', 'ajax')
    'qdznrexgjoltkblu'
    '''
    
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    # (1) Remove all spaces from the plaintext message before encryption
    plainText = plainText.strip()
    cipherText = ""

    # (2) Generate substitution cipher key from a password
    #       - Call 'genKeyFromPass' to do so
    cipherKey = genKeyFromPass(psw)

    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + cipherKey[idx]

    return cipherText 

doctest.testmod()



def substitutionDecrypt(cipherText, psw):
    '''
    (str, str) -> str

    Using the encrypted message, 'cipherText', from 'substitutionEncrypt',
    and the password used to generated the encryption key, the function
    will return the original plaintext message with spaces removed.
    
    Example:
    >>> substitutionDecrypt('qdznrexgjoltkblu', 'ajax')
    'thequickbrownfox'
    '''
    
    # (1) 'cipherText' is encrypted by 'substitutionEncrypt'
    plainText = substitutionEncrypt(cipherText, psw)

    return plainText

doctest.testmod()



def genKeyFromPass(password):
    '''
    (str) -> str

    Given a string the program returns a scrambled version of the alphabet
    using a password as the starting point.

    Calls on the function 'removeDupes(myString)'.
    '''

    key = 'abcdefghijklmnopqrstuvwxyz'
    password = removeDupes(password)

    lastChar = password[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx + 1:], password)
    beforeString = removeMatches(key[:lastIdx], password)

    key = password + afterString + beforeString

    return key


def removeDupes(myString):
    '''
    (str) -> str

    Removes duplicates from the password by reconstructing the string,
    one character at a time, using the accumulator pattern. The accumulator
    pattern adds a character to the 'newStr' function if it's not already a
    part of the reconstructed string. Otherwise, if it's already been added
    then it is ignored.

    Examples:
    >>> removeDupes('book')
    'bok'
    >>> removeDupes('topsecret')
    'topsecr'
    '''
    
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch

    return newStr

doctest.testmod()



def removeMatches(myString, removeString):
    '''
    (str, str) -> str

    Removes the characters from one string that are in another. With an
    empty string, 'myString' it accumulates to build a new string,
    'newStr'.
        - If the next character in the original string is not one of
          the characters in 'removeString' it is added to 'newStr'.
        - If the next character in 'myString is in 'removeString'
          it is ignored.

    Examples:
    >>> removeMatches('abcdefghijklmnopqrstuvwxyz', 'topsecr')
    'abdfghijklmnquvwxyz'
    >>> removeMatches('abcdefghijklmnopqrstuvwxyz', removeDupes('bondjamesbond'))
    'cfghiklpqrtuvwxyz' 
    '''
    
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch

    return newStr

doctest.testmod()




if __name__ == "__main__":
    main()

    












    



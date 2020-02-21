'''
Cluster analysis is a data mining technique that attempts to divide the data
into meaningful groups called clusters. These clusters represent data values
that show some kind of similarity to each other while exhibiting a dissimilar
relationship to data values outside of the cluster. 
'''



'''
- work with a SMALL file to start
- COMMENT OUT CLUSTER PRINTING
- set turtle speed to fastest: speed(0), speed(10), speed('fastest')
- "you'll need to add docstrings AND USEFUL IN-LINE COMMENTS"
    -> UNDERSTAND THE CODE
'''

'''
OPENING EXTERNAL FILES

# This method allows the file to be used only within the indented section
with open('filename.txt', 'r') as fileobj:
    ....
    ....
    ....
    .... do stuff
    ....
    ....

-----------------------------------------

# This method allows the file to be open to used throughout the program
# Needs to explicitly closed through
    - 'fileobj.close()'
# Program has limited amount of files that can be opened

fileobj = open('filename.txt', 'r')
fileobj.close()



Example:
>>> fileob = open("TEMP", "w")
>>> fileob.write("somestuff\n")
10
>>> fileob.close()

'''

# FILE OBJECTS ARE "iterable"

'''
MODES OF READING FILES:
    - 'r':
        -> opens for READ only
        -> safe
        -> error if one doesn't exist
    - 'w':
        -> open for WRITE only
        -> unsafe
        -> OVER writes contracts
        -> creates file if doesn't exist
    - 'a':
        -> same as 'write'
        -> doesn't override
'''

'''
WAYS OF READING FILES:
- '.read()':
    -> str
    -> everything
    -> moves file pointer to the end
- '.readline()':
    -> str
    -> one line
    -> file pointer moved by one line

- '.readlines()':
    -> list (string)
    -> everything
    -> file pointer moved to the end
'''



# TRY AND EXCEPT FUNCTIONS
# Also known as "exception handling"
# Google built-in Exception errors

'''
try:
    ... "protected by the 'except' block"
    ...
    ...

except:
    ... "what to do in case error(s)/Exception in 'try' block"
    ...
    ...

REASONS FOR USING TRY AND EXCEPT:
    - files
    - modules
    - arithmetic issues want to handle
    - bad user input























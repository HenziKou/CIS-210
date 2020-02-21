li = [2,4,6,8]

# accumlator loop pattern:

sum = 0
for item in li:
    sum+= item

# mapping loop pattern

newli = []
for etl in li:
    newli.append(elt*100)

# note - returns a list, so ....

newli2= [etl * 100 for elt in li]

#filter loop pattern

newli3 = []
for elt in li:
    if (elt % 4) == 0:
        newli3.append(elt)

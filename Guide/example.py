def rec(li,i):
    if i >= len(li):
        return 0
    else:
        return li[i] + rec(li, i+1)

def q4():
    ar = [ 1, 2, 3, 4, 5 ]
    t = rec(ar,0)

    print(t)

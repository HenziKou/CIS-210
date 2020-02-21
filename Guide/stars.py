def stars(n):
    if n == 1:
        print ('*')
    else:
        stars(n-1)
        print (n*'*')
        stars (n-1)

    return None

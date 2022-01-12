import collections
def func(string, n):
    length=len(string)
    d= {}
    for i in range(0, length - (n+1)):
        news= string[i: i+n]
        if news not in d:
            d[news]=0
        d[news] +=1
    return d

from collections import OrderedDict,Counter
def sortByFreq(arr,n):
    b = Counter(arr)
    #print(b)
    c = sorted (b.items(), key = lambda x: (-x[1],x[0]))
    #print(c)
    k = []
    for m in c:
        k.append(list(m))
    print(k)    
    z = []
    for i in k:
        while i[1] >0:
            z.append(i[0])
            i[1] -=1
    return z
    
    '''#code here
    d = OrderedDict({})
    for i in range(n):
        d[arr[i]] = d.get(arr[i],0)+1
    d = OrderedDict(sorted(d.items()))
    #print(d)
    m = {k:v for k,v in sorted(d.items(),key = lambda item:item[1],reverse=True)}
    
    #print(m)
    li = []
    for i in m.keys():
        print(i,m[i])
        while m[i]:
            li.append(i)
            m[i] -= 1
    print(*li)'''

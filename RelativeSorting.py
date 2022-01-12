from collections import OrderedDict
def relativeSort (A1, N, A2, M):
    # Your Code Here
    li = []
    d = {}
    for i in range(N):
        d[A1[i]] = d.get(A1[i],0)+1
    
    for i in range(M):
        if A2[i] in d.keys():
            while d[A2[i]]:
                li.append(A2[i])
                d[A2[i]] -= 1
            del d[A2[i]]
    
    d = OrderedDict(sorted(d.items()))
    #print(d)
    for i in d.keys():
        while d[i]:
            li.append(i)
            d[i] -= 1
            
    return li
    

def sortAbs(a, n, k):
    #code here
    b =[[0 for x in range(2)] for y in range(n)] 
      
    for i in range(0, n):  
        b[i][0] = abs(a[i]-k)  
        b[i][1] = i 
          
      
    b.sort()  
      
    for i in range(0, n):  
        a[i] = a[b[i][1]]
    return a


    '''d = {}
    for i in range(n):
        d[a[i]] = abs(k-a[i])
    d = sorted(d.items(),key= lambda x:(x[1],x[0]))

    for i in range(len(d)):
        a[i] = d[i][0]
    print(a)'''

def OddEvenSArray_E(a):
    
    n = len(a)
    curr = 1
    res = 1

    for j in range(1,n):
        
        if (a[j-1]%2 == 0 and a[j]%2 != 0) or (a[j-1]%2 != 0 and a[j]%2 == 0):
            curr +=1
            res = max(res,curr)
            
        else:
            curr = 1
    return res

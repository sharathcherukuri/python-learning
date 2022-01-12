def arthimeticArray(arr,n):
    d = 0
    curr,res = 0,0
    for i in range(1,n-1):
        d = arr[i] - arr[i-1]
        if d+arr[i] == arr[i+1]:
            curr += 1
            
        else:
            res = max(res,curr+(n-i)+1)
            curr = 0
    return res
    '''d = 0
    curr,res = 1,1
    for i in range(1,n-1):
        d = arr[i] - arr[i-1]
        if d+arr[i] == arr[i+1]:
            curr += 1
            res = max(res,curr)
        else:
            curr = 1
    return res+1'''
    

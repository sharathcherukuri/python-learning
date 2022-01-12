def longestArray(arr,s):
    d = {}
    pre_sum = 0
    
    res = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
    for i in range(len(arr)):
        pre_sum += arr[i]
        #print(pre_sum)
        if pre_sum == s:
            res = i+1
        if pre_sum not in d.keys():
            d[pre_sum] = i
        if abs(pre_sum - s) in d.keys():
            res = max(res,i-d[pre_sum-s])

    print(arr)
        
        
       
    return res 
    

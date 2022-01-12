def closer( arr, n,  x):
    #Your code here
    
    
    low =0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        if mid != 0 or mid != n-1:
            if arr[mid+1] == x:
                return mid+1
            elif arr[mid-1] == x:
                return mid-1
        
        if arr[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return -1

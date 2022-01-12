def threeWayPartition(arr, n, a, b):
    # Code here
    low = 0
    mid = 0
    high = n-1
    while mid <= high:
        if arr[mid] < a:
            arr[mid], arr[low] = arr[low],arr[mid]
            low  += 1
            mid += 1
        
        elif a<=arr[mid]<=b:
            mid += 1
            
        elif arr[mid] > b:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1
            
    return arr

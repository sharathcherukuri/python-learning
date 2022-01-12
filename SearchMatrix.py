def searchMatrix(arr,m,n,x):
    left = 0
    right = n-1
    top = 0
    bottom = m-1
    while left <= right  and top <= bottom:
        if x == arr[top][right]:
            return [top,right]
        elif x < arr[top][right]:
            right -= 1
        else:
            top += 1
    return -1

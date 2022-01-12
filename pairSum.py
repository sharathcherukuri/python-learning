def ispair(arr,sum):
    n = len(arr)
    s = set()
    for i in range(n):
        if sum-arr[i] in s:
            return True
        s.add(arr[i])
    return False

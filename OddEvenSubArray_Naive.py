def MaxoddEvenSArray(a):
    n = len(a)

    res = 1

    for i in range(n):
        curr =1
        for j in range(i+1,n):
            if (a[j-1]%2 == 0 and a[j]%2 != 0) or (a[j-1]%2 != 0 and a[j]%2 == 0):
                curr +=1
        res = max(res,curr)
    return res

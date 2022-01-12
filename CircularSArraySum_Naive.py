def maxCirSArray(a):
    n = len(a)

    res = a[0]

    for i in range(0,n):
        curr_max = a[i]
        curr_sum = a[i]
        for j in range(1,n):
            index = (i+j) % n
            curr_max += a[index]
            curr_sum = max(curr_sum,curr_max)

        res = max(res,curr_sum)
    return res

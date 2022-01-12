def buyAndSell(a):
    n = len(a)

    temp = [None]*n

    count = 0

    j =0

    for i in range(1,n):
        if a[i] > a[i-1]:
            temp[j] = i-1
            count += 1
            j += 1
        else:
            temp[j] = i-1
            print((temp[j-count],temp[j]))
            count  = 0
    print((temp[j-count],n-1))
    #print(temp)
    

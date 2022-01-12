def canFlower(f,n):
    j =0

    count = 0
    for i in range(1, len(f)-1):
        if f[i] == f[j]:
            f[i] = 1
            count +=1
            j+=1
        else:
            j+=1
    for i in range(len(f)):
        print (f[i])
    if n == count:
        return True
    else:
        return False
        

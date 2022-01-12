def GenerateBinary(n):
    # code here
    li = list()
    
    for i in range(1,n+1):
        #print(i)
        temp = i
        s = ""
        while temp:
            res = temp%2
            #print(res)
            s += str(res)
            temp = temp// 2
        s = s[::-1]
        li.append(int(s))
    return li

def rev(s:str,k:int):
    a= list(s)
    if (len(s) < k):
        print(s[::-1])
    else:
        for i in range(0,len(a),2*k):
            a[i:i+k] = reversed(a[i:i+k])
    return "".join(a)
            
        

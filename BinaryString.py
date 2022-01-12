def binarySubstring(n,s):
    #code here
    i = 0
    j = 1
    count = 0
    s = [str(x) for x in s]
    print(s)
    while i < n  and j<n:
        print("hi")
        if s[i] == 1 and s[j] == 1:
           
            count += 1
        #i += 1
        j += 1
        
    return count


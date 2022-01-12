from collections import Counter
def LongestDistinct(s):
    n = len(s)
    res = 0
    curr = 0
    k = 0
    for i in range(n):
        cnt = Counter(s[k:i])
        curr = 0
        #print(cnt)
        for j in cnt.keys():
            #print(j,"=",cnt[j])
            if cnt[j] == 1:
                curr += 1
                #print(curr)
                res = max(res,curr)
            else:
                #print("hi")
                
                #print(res)
                curr = 0
                k += 1
                #print(k)
                
            
        cnt = {}
    return res

        
    

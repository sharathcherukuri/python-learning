from collections import OrderedDict
def winner(arr,n):
    # Your code here
    # return the name of the winning candidate and the votes he recieved
    d = OrderedDict()
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] += 1
    m = max(d.values())
    li = []
    for i in d.keys():
        if d[i] == m:
            li.append([i,d[i]])
    #print(li)
    #li = [x for x in range(li) if li[i] <li[i-1]: else li[i-1]]
    if len(li) > 1:
        res = []
        res = li[0]
        for i in range(1,len(li)):
            if res[0] > li[i][0]:
                res = li[i]
            #res = min(res[0][0],li[i][0])
        return res
    else:
        return li[0]
            

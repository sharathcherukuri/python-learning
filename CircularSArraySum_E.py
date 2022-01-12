def maxSArray(a):
    n = len(a)

    max_e = a[0]
    res = a[0]
    min_e = a[0]

    for i in range(1,n):
        max_e = max(max_e+a[i],a[i])
        res = max(res,max_e)
    return res

def minsum(a):
    sf = a[0]
    se = a[0]
    ts = 0
    for i in a:
        ts+=i
    for i in range(1,len(a)):
        sf = min(sf+a[i],a[i])
        se = min(se,sf)
    cir_sum = ts - se
    return cir_sum
def maxCirSArray(a):
    if maxSArray(a) < 0:
        return maxSArray(a)
    return max(maxSArray(a),minsum(a))



        

import collections
def maxStep(height):
    #Your code here
    n= len(height)
    lmax = [0]*n
    rmax = [0]*n
    lmax[0]= height[0]
    res = 0
    for i in range(1,n):
        lmax[i] = max(height[i],lmax[i-1])
    rmax[n-1] = height[n-1]
    for i in range(n-2,0,-1):
        rmax[i] = max(height[i],rmax[i+1])
    print(lmax,rmax)
    for i in range(1,n-1):
        res = res+(min(lmax[i],rmax[i])-height[i])
    return res

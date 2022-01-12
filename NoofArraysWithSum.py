from collections import OrderedDict
def subArraySum(arr, n, sum):
    #Your code here
    mp = OrderedDict({})
    pre_sum = 0
    count  = 0
    for i in range(n):
        pre_sum += arr[i]
        if pre_sum == sum:
            count +=1
        x = mp.get(pre_sum-sum,False)
        print(x)
        if x is not False:
            count += x
        mp[pre_sum] = mp.get(pre_sum,0)+1
    print(mp)
    return count
    

def sumzero():
    nums = [-1,0,1,2,-1,-4]
    l=[]
    for i in range(0,len(nums)):
       for j in range(i+1,len(nums)):
           for k in range(j+1,len(nums)):
               if nums[i]+nums[j]+nums[k] == 0:
                   l+=[[nums[i],nums[j],nums[k]]]
               else:
                    break
    return l

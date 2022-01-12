from operator import itemgetter
def fourSum(nums, target):
    a= []
    n =  len(nums)
    nums = sorted(nums)
    #print(nums)
    for i in range(0,n-3):
        if i!=0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j != i+1 and nums[j] == nums[j-1]:
                continue
            left = j+1
            right = n-1
            while(left < right):
                sum = nums[i]+nums[j]+nums[left]+nums[right]
                if (sum < target):
                    left+=1
                elif (sum > target):
                    right-=1
                else:
                    a.append([nums[i],nums[j],nums[left],nums[right]])
                    #print(a)
                    left+=1
                    right-=1
                while(left < right and nums[left] == nums[left-1]):
                    left+=1
         
                while(left < right and nums[right] == nums[right+1]):
                    right-=1
            

    return sorted(a)
                
        
        

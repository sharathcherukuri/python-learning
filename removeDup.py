def removeDup(nums,val):
    n =  len(nums)
    j =0
    for i in range(1,n):
        if nums[j] == val and nums[i] != val:
            nums[j] = nums[i]
            j+=1
        else:
            continue
    return j+1
            
    
    

    
    

'''
So How to Find, if array is Decreasingly or Increasingly Sorted in a Sorted and Rotated Array.

Simple,

If the positon of Max. Element is just before Min. Element, then it is Increasingly Sorted
Else if position of Max. Element is just after Min. Element then it is Decreasingly Sorted,
Else it is not sorted and rotated.
So now What to do..??
In case of Increasingly Sorted,

Check if array is increasing upto Max. Element
Check if array is increasing again after Min Element
Check if Last Element is smaller than the first element
In case of Decreasingly Sorted,

Check if array is decreasing upto Min. Element
Check if array is decreasing again after Max Element
Check if Last Element is larger than the first element
If all these conditions meet, the array is sorted and rotated'''

def checkRotatedAndSorted(arr,n):
    #code here
    maxe = max(arr)
    mine = min(arr)
    flaga = False
    flagb = False
    flagc = False
    for i in range(n):
        if arr[i] == maxe:
            maxi = i
        elif arr[i] == mine:
            mini = i
    print(maxi,mini)
    
    if maxi == (mini-1):
        i = 0
        if arr[0] > arr[n-1]:
            flagc = True
        while(i < n):

            while(i<=maxi):
                if arr[i] > arr[i-1]:
                    flaga = True
                    i += 1
                else:
                    flaga = False
                    i += 1
            while(i != n-1):
                if arr[i] < arr[i+1]:
                    flagb  = True
                    i +=1 

                else:
                    flagb = False
                    i += 1
            i += 1

    elif maxi == mini+1:
        i = 0
        if arr[0] < arr[n-1]:
            flagc =  True
        while(i < n):

            while( i <= mini):
                if arr[i] < arr[i-1]:
                    flaga = True
                    i += 1
                else:
                    flaga = False
                    i += 1
            while( i != n-1):
                if arr[i] > arr[i+1]:
                    flagb = True
                    i += 1
                else:
                    flagb = False
                    i += 1
            i += 1
    print(flaga,flagb,flagc)
    if flaga and flagb and flagc:
        return True
    else:
        return False
                    
    
            
                
        
    

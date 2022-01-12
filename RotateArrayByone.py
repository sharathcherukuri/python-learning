import sys
def MaxsubArray(a):
    sum_e = 0
    sum_f = 0

    for i in range(len(a)):
        sum_f += a[i]
        for j in range(i+1,len(a)):
            sum_f += a[j]

            if sum_f > sum_e:
                sum_e = sum_f
        sum_f =0
    return sum_e
     
                        
            
            

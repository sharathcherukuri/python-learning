def majorityWins(a, n,  x,y):
    # code here
    
    count_x = 0
    count_y = 0
    for i in range(0,n):
        if x == a[i]:
            count_x += 1
        elif y == a[i]:
            count_y += 1
    if count_x > count_y:
        return x
    elif count_x < count_y:
        return y
    elif count_x == count_y:
        if  x < y:
            return x
        else:
            return y
            
        

    

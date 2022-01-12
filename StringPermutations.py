def recurex(d,res):
    if d == 0:
        return 0
    res += (d%10)
    recurex(d//10,res)
    recurex(res,res)
    return res
        
    
    
    

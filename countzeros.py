def gcd(a,b):

    if a < b:
        
        for i in range(a,1,-1):
       
            if a % i == 0 and b % i == 0:
                return i
            else:
                return 1
               
    elif b < a:
        for i in range(b,1,-1):
             if a % i == 0 and b % i == 0:
                return i
             else:
                return 1
   

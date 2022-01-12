def nthprimedigitsnumber(n):
    
    # print:  Nth number made of prime digits
    #25 27 32 33 35 37 52 53 55 57 72 73 75 77 222 223 225 227 
    prime = [""]*100
    prime[0] = '2'
    prime[1] = "3"
    prime[2] = "5"
    prime[3] = "7"
    j = 0
    k = 0
    for i in range(4,100):
        prime[i] += prime[j]+prime[k] 
        k += 1
        if k == 4:
            k = 0
            j += 1
    print(prime)            
    return prime[n-1]

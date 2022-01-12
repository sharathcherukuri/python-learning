import math
def quadraticRoots(a,b,c):
    #Your code here
    if a == 0:
        print("roots are invalid")
        return -1
    des = b * b - 4*a*c
    sqrt_a = math.sqrt(abs(des))
    
    if des == 0:
        print("{:g}".format(-b/(2*a)),"{:g}".format(-b/(2*a)))
        #print(-b/(2*a),-b/(2*a))
    elif des > 0:
        print((-b + sqrt_a)/(2 * a))
        print("{:g}".format((-b + sqrt_a)/(2 * a))) 
        print("{:g}".format((-b - sqrt_a)/(2 * a)))
    else:
        print("imaginary")

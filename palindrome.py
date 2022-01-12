def palindrome(x)->bool:
    k=x
    if(k < 0 or k is None or type(k) is not int):
        print(hello)
        return False
    else:
        reverse=0
        while k>0:
            r = k % 10
            reverse = (reverse*10)+r
            k =k /10
        print(reverse)
    if x == reverse:
        return True
    else:
        return False

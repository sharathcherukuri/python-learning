def intToRoman(num: int) -> str:
    itor = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',
            90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    i = 12
    l=[]
    s=''
    for k in itor.keys():  
        l.append(k)
    print(l)
    while num:
        q = num // l[i]
        num = num % l[i]
        print("q={0} num={1}".format(q,num))
        while q:
            s=s + ''.join(itor.get(l[i]))
            print(s)
            q -=  1
        i-=1
    print(s)

            
        

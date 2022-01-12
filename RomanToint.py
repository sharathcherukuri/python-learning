def romanToInt(s:str):
    rtoi = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,
            'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    num=0
    l=['IV','IX','XL','XC','CD','CM']
    for i in l:
        if i in s:
            num+= rtoi.get(i)
            #print(num)
            k= s.index(i)
            s= s[:k]+s[k+2:]
            #print(s)
    for i in s:
        num += rtoi.get(i)
    print(num)
     

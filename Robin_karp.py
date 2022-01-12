def robinKarp(txt,pat,q,d):
    n = len(txt)
    m = len(pat)
    h = 1
    for i in range(1,m):
        h = (h*d)%q
    p =0
    t = 0
    for i in range(m):
        p = (p*d + ord(pat[i]))%q
        t = (t*d + ord(txt[i]))%q
    for i in range(n-m+1):
        if p == t:
            flag = True
            for j in range(m):
                if pat[j]!= txt[i+j]:
                    flag = False
                    break
            if flag == True:
                print(i,end = " ")
        if i < n-m:
            t = (d*(t- txt[i]*h)+txt[i+m])%q
        if t<0:
            t = t+q

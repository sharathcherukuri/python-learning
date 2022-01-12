def gcd(s):
    b = ""
    j = 0
    for i in range(len(s)):
        print(s[i])
        if s[i] == " ":
            print("hi")
            b += s[j:i:-1]
            j = i
    return b

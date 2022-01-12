def rev_vow(s:str):
    vow =['a','e','i','o','u']
    def helper(left, right):
        if left < right:
            print("hi")
            if s[left] in vow and s[right] in vow:
                print("hi")
                s[left], s[right] = s[right], s[left]
                print(s[left],s[right])
                helper(left + 1, right - 1)
            else:
                helper(left + 1, right - 1)
    helper(0, len(s) - 1)
    print(s)



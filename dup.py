import collections
def func(str, n):
    n = int(n)

    length = len(str)

    st = collections.defaultdict()

    for i in range(0, length - n + 1):
	newStr = str[i : i + n]
        if newStr not in st:
            st[newStr]=0
	st[newStr]+=1
    return st



func("AGCTTCGAGATCCTAGTTTCGAGATCGATCGGGACTGATCGGGACAATGCAATAGACCCHTHTHTHGGCTAHGAHATH", "2")

no_of_chars = 256
def leftRepeat(s):
    res = -1
    n = len(s)
    visited = [False]*256
    for i in range(n-1,-1,-1):
        if visited[ord(s[i])] == False:
            visited[ord(s[i])] = True
        else:
            res = i
    return res

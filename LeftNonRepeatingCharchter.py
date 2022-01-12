no_of_chars = 256
import sys
def leftNonRepeat(s):
    visited = [0]*no_of_chars
    n = len(s)
    res = sys.maxsize
    for i in range(n):
        visited[ord(s[i])] += 1
    for i in range(256):
        if visited[i]:
            print(chr(i),"->",visited[i])
    for i in range(n):
        if visited[ord(s[i])] == 1:
             return i
    
    return -1

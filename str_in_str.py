def strStr(haystack: str, needle: str):
    if haystack == needle or needle== "":
        return 0
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
        

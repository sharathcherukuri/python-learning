def longestprefix(strs):
    l_prefix=""
    shortest_str= min(strs,key=len)
    if not strs:
        return l_prefix
    for i in range(0,len(shortest_str)):
        if(all([x.startswith(shortest_str[:i+1]) for x in strs])):
            l_prefix= shortest_str[:i+1]
        else:
            break
    return l_prefix
        

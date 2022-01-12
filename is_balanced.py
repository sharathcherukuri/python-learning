def is_balanced(text, braces="()[]{}<>"):
    counts={}
    left_to_right={}
    for left, right in zip(braces[::2],braces[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left]=0
        left_to_right[right]=left
    for c in text:
        if c in counts:
            counts[c]+=1
        else:
            left = left_to_right[c]
            if counts[left]== 0:
                return False
            counts[left]-=1
    return not any(counts.values())
        

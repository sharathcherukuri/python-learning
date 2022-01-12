import itertools as it
def letterCombinations1(digits: str):
    d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    l=[]
    b=[]
    c=[]
    for i in digits:
        if i not in ['0','1']:
            l.append(d[i])
    return [''.join(xx) for xx in it.product(*l) if xx]
    
    

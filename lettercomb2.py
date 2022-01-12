import itertools as it
def letterCombinations(digits: str):
        m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        possibilities = [m[xx] for xx in digits if not xx in ['0', '1']]
        print(possibilities)
        return [''.join(xx) for xx in it.product(*possibilities) if xx]

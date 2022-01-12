def generateparath(n:int):
    sol=[]
    def backtrack(s='',left=0,right=0):
        if len(s) == n*2 :
            sol.append(s)
        if left < n:
            backtrack(s+'(',left+1,right)
            #print(s)
        if right < left :
            backtrack(s+')',left,right+1)
            print(s)
        
    backtrack()
    return sol

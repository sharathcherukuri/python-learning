from collections import deque
def bal_parenthesis(s):
    d = {')':'(','}':'{',']':'['}
    stack = deque()
    n = len(s)
    for i in range(n):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            elif d.get(s[i]) != stack.pop():
                return False
            else:
                stack.pop()
    return True

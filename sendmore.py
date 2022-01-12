import constraint
problem = constraint.Problem()

problem.addVariables('S',range(1,10))
problem.addVariables('M',range(1,10))
problem.addVariables('E',range(0, 10))
problem.addVariables('N',range(0, 10))
problem.addVariables('D',range(0, 10))
problem.addVariables('O',range(0, 10))
problem.addVariables('R',range(0, 10))
problem.addVariables('Y',range(0, 10))

def o(s,e,n,d,m,o,r,y):
    if(s*1000 + e*100 + n*10 + d + m*1000 + o*100 + r*10 + e) == (10000*m + 1000*o + 100*n + 10*e + y):
        return True

problem.addConstraint(o, ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'])

problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()
print(solutions)

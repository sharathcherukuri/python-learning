import cmath
import math
import sys

def get_float(msg, allow_zero):
    x= None
    while x is None:
        try:
            x= float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x= None
        except ValueError as err:
            print(err)
    return x

print("ax\N{SUPERSCRIPT TWO}+bx+c = 0")
a= get_float("enter a:", False)
b= get_float("enter b:", True)
c= get_float("enter c:", True)

x1= None
x2= None

d = b**2- 4*a*c

if d==0:
    x= -(b/(2*a))
elif d > 0:
    root = math.sqrt(d)
else:
    root = cmath.sqrt(d)
x1 = (-b+root) / (2*a)
x2 = (-b-root) / (2*a)

Equation = ("{0}x\N{SUPERSCRIPT TWO}+{1}x+{2} = 0" "\N{RIGHTWARDS ARROW} x = {3}"). format(a,b,c,x1)

if x2 is not None:
    Equation += "or x ={0}".format(x2)
print(Equation)

import math
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

if b == 0:
    print("Second argment cannot be 0")
else:
    x = (math.sqrt(a*b))/(((math.e)**a)*b) + (a*((math.e)**(2*a/b)))
    print(x)


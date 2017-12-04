# TASK:
# Вхідні дані: 2 невід'ємних дійсних числа a та b -- аргументи командного рядка. b не дорівнює 0.
# Вихідні дані: дійсне число -- результат обчислення формули

# SOLUTION:
# Importing modules to work with embedded functions
import math
import sys

# Assigning variables values of two first cmd-line arguments
a = float(sys.argv[1])
b = float(sys.argv[2])

# Divider error check (second argument shouldn't be zero)
if b == 0:
    print("Second argment cannot be 0")
else:
    x = (math.sqrt(a*b))/(((math.e)**a)*b) + (a*((math.e)**(2*a/b)))
    print(x)

# TASK:
# Вхідні дані: 3 дійсних числа -- аргументи командного рядка.
# Вихідні дані: результат обчислення формули

# SOLUTION:
# Importing modules to work with embedded functions
import sys
import math 

# Assigning variables values of three cmd-line arguments
x = float(sys.argv[1])
mu = float(sys.argv[2])
sigma = float(sys.argv[3])

# Calculate given formula
result = (1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((math.pow((x-mu), 2)/2*sigma**2)))

print(result)

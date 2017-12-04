# TASK:
# Вхідні дані: 3 дійсних числа a, b, c. Передаються в програму як аргументи командного
# рядка.
# Результат роботи: рядок "triangle", якщо можуть існувати відрізки з такою довжиною та з
# них можна скласти трикутник, або "not triangle" якщо ні.

# SOLUTION:
# Importing modules to work with embedded functions
import sys

# Assigning variables values of three cmd-line arguments
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

# Checks if there is possibility to create triangle from input numbers
if a + b > c and a + c > b and b + c > a:
    print("triangle")
else:
    print("not triangle")
    
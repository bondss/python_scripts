# TASK:
# Вхідні дані: ціле невід'ємне число n. Передається в програму як аргумент командного
# рядка.
# Результат роботи: значення n-го числа послідовності Фібоначчі. Не використовувати рекурсію

# SOLUTION:
# Importing modules to work with embedded functions
import sys

n = int(sys.argv[1])
a_0 = 0
a_1 = 1

# Fibonacci sequence without recursion
if n < 0:
    print("n cannot be negative number")
else:
    for i in range(0, n):
        temp = a_0
        a_0 = a_1
        a_1 = temp + a_1
    print(a_0)

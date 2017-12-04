# TASK:
# Вклад в банке составляет x грн. Ежегодно он увеличивается на p процентов.
# Определите, через сколько лет вклад составит не
# менее y грн.
# Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое
# число.

# SOLUTION:
import sys

x = int(sys.argv[1])
p = int(sys.argv[2])
y = int(sys.argv[3])
years = 0

while x < y:
    x = x + x * (p / 100)
    years += 1

print(years)

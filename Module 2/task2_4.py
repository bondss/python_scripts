# TASK:
# Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один
# раз разломить по прямой на две части. Определите, можно ли таким образом отломить от
# шоколадки часть, состоящую ровно из k долек. Программа получает на вход три числа: n, m, k
# и должна вывести YES или NO.

# SOLUTION:
import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
k = int(sys.argv[3])

# Overall area must be bigger than parts number
if (n * m) < k:
    print("NO")
elif k % n == 0 or k % m == 0: # At least one dimension must divide with remainder equal to 0
    print("YES")
else:
    print("NO")

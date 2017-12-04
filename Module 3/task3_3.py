# TASK:
# Розробити функцію super_fibonacci(n, m),
# яка приймає 2 аргументи -- додатні цілі числа n та m (0 < n, m <= 35),
# та повертає число -- n-й елемент послідовності супер-Фібоначчі порядку m.

# SOLUTION:
def super_fibonacci(n, m):
    # due to task first m elements - are ones
    if n <= m:
        return 1
    # otherwise calculate
    else:
        # initializing variable for sum
        summ = 0
        # adding m previous numbers of sequence, using recursion
        for i in range(1, m+1):
            previous = super_fibonacci(n-i, m)
            summ = summ + previous
        # return sum as last n-element value
        return sum

# Test suite:
print(super_fibonacci(2, 1))
print(super_fibonacci(3, 5))
print(super_fibonacci(8, 2))
print(super_fibonacci(9, 3))

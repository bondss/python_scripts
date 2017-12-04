# TASK:
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка
# потерялась. Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

# SOLUTION:
N = int(input())

sum_all = 0
sum_k = 0

# Firstly, calculate sum of all numbers in range 1 to input
for i in range(1, N + 1):
    sum_all += i

# Then, we input numbers that remain and summarize them
for i in range(1, N):
    n = int(input())
    sum_k += n

# Number of lost card is calculated this way:
print(sum_all - sum_k)

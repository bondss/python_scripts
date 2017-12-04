# TASK:
# Вхідні дані: довільна, відмінна від нуля, кількість значень - аргументів командного рядка.
# Результат роботи: рядок, що складається з отриманих значень в зворотньому порядку,
# записаних через пробіл. Пробіл в кінці рядка відсутній.

# SOLUTION:
import sys

my_list = sys.argv[1:]

my_list.reverse() # reverse returns all arguments as one string
print(" ".join(my_list)) # so we use "join" to add whitespaces

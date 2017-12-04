# TASK:
# два цілих невід'ємних числа (0<=a1<=a2<=999999) - аргументи командного
# рядка.
# Результат роботи: кількість "щасливих квитків", чиї номери лежать на проміжку від a1 до
# a2 включно.

# SOLUTION:

import sys
a1 = int(sys.argv[1])
a2 = int(sys.argv[2])

# Initializing variables
input_str = ''
counter = 0

# Including last value in loop
for i in range(a1, a2+1):
    input_str = str(i) # convert and working with strings
    zeros = 6 - len(input_str) # calculating number of zeros to add
    input_str = zeros * "0" + input_str # adding them
    # checking if sum of first 3 numbers is equal to second
    if (int(input_str[0]) + int(input_str[1]) + int(input_str[2])) == (int(input_str[3]) + int(input_str[4]) + int(input_str[5])):
        counter = counter + 1
print(counter) # print overall quantity of such "happy tickets"

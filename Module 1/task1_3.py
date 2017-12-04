# TASK
# Вхідні дані: 3 числа x, y та z. x, y -- невід'ємні цілі числа, z дорівнює 0 або 1. x не дорівнює 0
# Передаються як аргументи командного рядка.
# Вихідні дані: рядок "Everybody sing a song: <текст пісеньки>", де <текст пісеньки>
# формується з у куплетів, розділених пробілами. Всі куплети однакові і складаються з x 'la'
# через дефіс. Якщо z дорівнює одиниці, в кінці ставиться окличний знак, інакше крапка. За
# відсутності куплетів пробіл перед крапкою/окличним знаком не ставиться.

# SOLUTION
# Importing modules to work with embedded functions
import sys

# Assigning variables values of three cmd-line arguments
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Defining constant part of song
const = "Everybody sing a song: "

# Performing checks due to task
if x > 1:
    couplet = y*((x*("la"  + "-" ))[:-1]+ " ")
else:
    couplet = y*((x*"la" + " "))

if y == 0:
    if z == 1:
        print(const [:-1]  + couplet [:-1] + "!")
    elif z == 0:
        print(const [:-1] + couplet [:-1] + ".")
else:
    if z == 1:
        print(const + couplet [:-1] + "!")
    elif z == 0:
        print(const + couplet [:-1] + ".")

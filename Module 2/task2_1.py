# TASK:
# Вхідні дані: рядок, що складається з відкриваючих та закриваючих круглих дужок -
# аргумент командного рядка. Для передачі в якості рядка послідовність береться в подвійні
# лапки.
# Результат роботи: рядок "YES", якщо вхідний рядок містить правильну дужкову
# послідовність; або рядок "NO", якщо послідовність є неправильною.

import sys
string = sys.argv[1]

# Initializing variables
count = 0
flag = True

# Checking count of brackets
for char in string:
    if char == "(":
        count = count + 1
    elif char == ")":
        count = count - 1
    if count < 0:
        flag = False
if flag and count == 0: # Assure that brackets order is correct
    print("YES")
else:
    print("NO")

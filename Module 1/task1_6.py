# TASK:
# Вхідні дані: рядок, передається в програму як аргумент командного рядка. Може містити
# пробіли, літери латинського алфавіту в будь-якому регістрі та цифри. Для передачі одним
# значенням рядок, що містить пробіли, береться в подвійні лапки.
# Результат роботи: рядок "YES", якщо отриманий рядок є паліндромом, або "NO" - якщо
# ні.

# SOLUTION:
import sys

example_string = str(sys.argv[1])

# Removing whitespaces and performing check
example_string = example_string.replace(" ", "")
if example_string.lower() == example_string.lower()[::-1]: # slice [::-1] reverses string
    print("YES")
else:
    print("NO")

# TASK:
# Розробити функцію counter(a, b),
# яка приймає 2 аргументи -- цілі невід'ємні числа a та b,
# та повертає число -- кількість різних цифр числа b, які містяться у числі а.

# SOLUTION:
def counter(a, b):
    num = 0
    a_str = str(a)
    b_str = str(b)
    found = ''
    for char_b in b_str:
        if a_str.find(char_b) != -1 and found.find(char_b) == -1:
            num = num + 1
            found = found + char_b
    return num

# Test suite
print(counter(12345, 567))
print(counter(1233211, 12128))
print(counter(123, 45))

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

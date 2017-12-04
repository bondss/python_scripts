import sys

def clean_list(list_to_clean):
    found = []
    for element in list_to_clean:
        flag = False
        for i in found:
            if i == element and str(i) == str(element):
                flag = True
        if not flag:
            found.append(element)
    return found

# Test suite
print(clean_list([1, 1.0, '1', -1, 1]))
print(clean_list(['qwe', 'reg', 'qwe', 'REG']))
print(clean_list([32, 32.1, 32.0, -123]))
print(clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]))

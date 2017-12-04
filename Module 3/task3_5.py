# TASK:
# Розробити функцію count_holes(n),
# яка приймає 1 аргумент -- ціле число або рядок, який містить ціле число,
# та повертає ціле число -- кількість "отворів" у десятковому записі цього числа друкованими цифрами
# (вважати, що у "4" та у "0" по одному отвору),
# або рядок ERROR, якщо переданий аргумент не задовольняє вимогам: є дійсним або взагалі не числом

# SOLUTION:
def count_holes(n):
    # convert to string
    n = str(n)
    # if number is negative, remove minus
    if n != '' and n[0] == '-':
        n = n[1:]
    # if number is empty, return error
    if n is '':
        return 'ERROR'
    # declare dictionary with pre-defined holes
    hole_draft = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1}
    # define must-have conditions
    chars_allowed = list(hole_draft.keys())
    not_zero_chars = chars_allowed[:]
    not_zero_chars.remove('0')
    counter = 0
    # using this variable for skipping leading zeroes
    number_started = False
    # looping through digits
    for char in n:
        # if we find char not corresponding to above conditions
        if not(char in chars_allowed):
            return 'ERROR'
        # if current digit is not zero, flip flag-variable and start count holes
        if char in not_zero_chars:
            number_started = True
        # incrementing counter by adding number of hole in current digit
        if number_started:
            counter = counter + int(hole_draft[char])
    if not number_started:
        counter = 1
    # return result
    return counter

# Test suite
print(count_holes(-8))
print(count_holes('123'))
print(count_holes(906))
print(count_holes('001'))
print(count_holes(-8.0))

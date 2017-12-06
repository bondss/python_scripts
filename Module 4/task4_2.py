# TASK:
# Написать программу поиска самого длинного слова в строке, разделенной пробелами.

# SOLUTION:
def find_longest_word(word_list):
    # Searching for the max word length in list
    # using length as a key of "max" method
    longest_word = max(word_list, key=len)
    return longest_word

# Asking user for input
words = input()
# Form list divided by whitespaces using split method
formList = words.split()
# Display result of function
print(find_longest_word(formList))

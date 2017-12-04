# TASK:
# Вхідні дані: рядок, передається в програму як аргумент командного рядка. Може містити
# пробіли та літери латинського алфавіту в будь-якому регістрі. Для передачі в якості
# одного аргументу рядок береться в подвійні лапки.
# Результат роботи: рядок - дешифроване повідомлення.

# SOLUTION:
import sys

# Set key due to task
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ciphertext = str(sys.argv[1])
ciphertext = ciphertext.replace(' ', '') # Removing whitespaces
if len(ciphertext) % 5 > 0:
    ciphertext = ciphertext[:-(len(ciphertext) % 5)] # Splitting ciphertext to 5-symbol groups
abcode = ""
for letter in ciphertext:
    if letter == letter.lower(): # At first: convert ciphertext to 'ab' sequences
        abcode += 'a'
    else:
        abcode += 'b'
i = 0
new_index = 0
decode = ""
for i in range(0, len(abcode) // 5): # Again, split 'ab' sequence to 5-symbol groups
    start = key.find(abcode[new_index:(new_index + 5)]) # Find starting index of 5-symbol key sequence
    letter = alphabet[start] # looking for that index in alphabet and corresponding letter
    decode += letter # Write letter in final array
    new_index = new_index + 5 # Go to next 5-symbol key sequence
    i += 1 
print(decode)

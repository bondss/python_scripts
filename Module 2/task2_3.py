import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ciphertext = str(sys.argv[1])
ciphertext = ciphertext.replace(' ', '')
if len(ciphertext) % 5 > 0:
    ciphertext = ciphertext[:-(len(ciphertext) % 5)]
abcode = ""
for letter in ciphertext:
    if letter == letter.lower():
        abcode += 'a'
    else:
        abcode += 'b'
i = 0
new_index = 0
decode = ""
for i in range(0, len(abcode) // 5):
    start = key.find(abcode[new_index:(new_index + 5)])    
    letter = alphabet[start]
    decode += letter
    new_index = new_index + 5
    i += 1
print(decode)

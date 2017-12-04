# TASK:
# Розробити функцію encode_morze(text),
# яка приймає 1 аргумент -- рядок,
# та повертає рядок, який містить діаграму сигналу, що відповідає переданому тексту,
# закодованому міжнародним кодом Морзе для англійського алфавіту.
# Розділові та інші знаки, що не входять до латинського алфавіту, ігнорувати.
# Регістром літер нехтувати.


# SOLUTION:
def encode_morze(text):
    # define dictionary for text conversion
    morze = {
        "A" : ".-", 
        "B" : "-...", 
        "C" : "-.-.", 
        "D" : "-..", 
        "E" : ".", 
        "F" : "..-.", 
        "G" : "--.", 
        "H" : "....", 
        "I" : "..", 
        "J" : ".---", 
        "K" : "-.-", 
        "L" : ".-..", 
        "M" : "--", 
        "N" : "-.", 
        "O" : "---", 
        "P" : ".--.", 
        "Q" : "--.-", 
        "R" : ".-.", 
        "S" : "...", 
        "T" : "-", 
        "U" : "..-", 
        "V" : "...-", 
        "W" : ".--", 
        "X" : "-..-", 
        "Y" : "-.--", 
        "Z" : "--..", 
    }
    encoded = ''
    # starting per-symbol looping
    for i in text:
        # form fragment to add
        to_add = ''
        # if we find a whitespace, replace with pause
        if i == ' ':
            to_add = '____'
        # convert to upperсase and looking in dictionary
        elif i.upper() in morze.keys():
            # replace dots/dashes with corresponding signals, also
            # add pause after every word
            to_add = morze[i.upper()].replace('.', '^_').replace('-', '^^^_') + '__'
        encoded = encoded + to_add
    
    # check for extra pauses in the end and remove them
    if len(encoded):
        while encoded[-1] == '_':
            encoded = encoded[:-1]
    
    return encoded

# Test suite
print(encode_morze('Morze code'))
print(encode_morze('Prometheus'))
print(encode_morze('SOS'))
print(encode_morze('1'))

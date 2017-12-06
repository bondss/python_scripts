# TASK:
# Написать программу декодирования телефонного номера для АОН.
# По запросу АОНа АТС посылает телефонный номер, используя следующие правила:
# — Если цифра повторяется менее 2 раз, то это помеха и она должна быть отброшена
# — Каждая значащая цифра повторяется минимум 2 раза
# — Если в номере идут несколько цифр подряд,
# то для обозначения «такая же цифра как предыдущая» используется идущий 2 и более подряд раз знак #

# SOLUTION:
from functools import reduce
def aon(s):
    # Remove single digits
    s = ''.join(map(lambda x: x[1] if x[0] == x[1] else '', zip(s[1:], s)))
    # Remove duplicates
    s = reduce(lambda x, y: x + y if x[-1] != y else x, s)
    # Decode '#'
    s = reduce(lambda x, y: x + x[-1] if y == '#' else x + y, s)
    # Remove leading '#'
    s = s.strip('#')
    return s

# Test suite
print(aon("###1111233343322#221#235555###1"))
print(aon("4434###552222311333661"))

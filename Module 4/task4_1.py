# TASK:
# Написать программу, выводящую заданную пользователем строку как минимум в 3 разных кодировках.
# При этом писать вызов метода encode() в программе можно только 1 раз.

# SOLUTION:
# Set test string
s = '\u041f\u0440\u0438\u0432\u0435\u0442'

# define 3 encodings in loop
for enc in ["cp1251", "utf-8", "koi8-r"]:
    # print output in each
    print(s.encode(enc))
    
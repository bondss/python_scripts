# TASK: 
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из
# чисел от 1 до i без пробелов.

# SOLUTION:
import sys

num = int(sys.argv[1])

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end = "") # replace newline with nothing when print one ladder
    print() # print newline after every ladder

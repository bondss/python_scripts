import sys

n = int(sys.argv[1])
a_0 = 0
a_1 = 1

if n < 0:
    print("n cannot be negative number")
else:
    for i in range(0, n):
        temp = a_0
        a_0 = a_1
        a_1 = temp + a_1
    print(a_0)

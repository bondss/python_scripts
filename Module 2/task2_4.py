import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
k = int(sys.argv[3])

if (n * m) < k:
    print("NO")
elif (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")

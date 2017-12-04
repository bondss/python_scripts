import sys

x = int(sys.argv[1])
p = int(sys.argv[2])
y = int(sys.argv[3])
years = 0

while (x < y):
    x = x + x * (p / 100)
    years += 1

print(years)

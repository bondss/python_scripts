import sys
a1 = int(sys.argv[1])
a2 = int(sys.argv[2])

input_str = ''
counter = 0

for i in range(a1, a2+1):
    input_str = str(i)
    zeros = 6 - len(input_str)
    input_str = zeros * "0" + input_str
    if (int(input_str[0]) + int(input_str[1]) + int(input_str[2])) == (int(input_str[3]) + int(input_str[4]) + int(input_str[5])):
        counter = counter + 1
print(counter)

N = int(input())

sum_all = 0
sum_k = 0

for i in range(1, N + 1):
    sum_all += i

for i in range(1, N):
    n = int(input())
    sum_k += n

print(sum_all - sum_k)

import sys
# 3
# 1 2 3
t = int(input())
k = sys.stdin.read().split()
A = (k[:t])
odd_pair = 0
even_pair = 0
for i in range(t - 1):
    for j in range(i + 1, t):
        if (int(A[i]) + int(A[j])) % 2 != 0:
            odd_pair += 1
        elif (int(A[i]) + int(A[j])) % 2 == 0:
            even_pair += 1
print(odd_pair - even_pair)

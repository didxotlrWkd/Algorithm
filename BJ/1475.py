import sys

input = sys.stdin.readline

N = list(input().strip())
L = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(N)):
    L[int(N[i])] += 1

L[6] = ((L[6] + L[9]) // 2) + ((L[6] + L[9]) % 2)
L[9] = 0
print(max(L))  
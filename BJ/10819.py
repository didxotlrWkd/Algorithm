import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

pers = list(permutations(A , N))

max = 0

for per in pers:
    result = 0
    for i in range(1,len(per)):
        result += abs(per[i-1] - per[i])
    if max < result :
        max = result
    
print(max)
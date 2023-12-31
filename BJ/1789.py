import sys

input = sys.stdin.readline

S = int(input())

sum = 0
i = 1
count = 0

while S != sum:
    if S - sum >= i:
        sum += i
        i += 1
        count += 1
    else:
        sum -= i-1
        sum += i

print(count)        


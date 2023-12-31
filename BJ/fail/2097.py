import sys

input = sys.stdin.readline

N = int(input())

x = -1
y = -1

for _ in range(4,N):
    if x <= y:
        x += 1
    else :
        y+=1

print(f"{x} , {y}")

0,0
0,1
1,0
1,1
2,0
2,1
0,2
1,2
2,2
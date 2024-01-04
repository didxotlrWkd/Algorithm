import sys
from collections import deque

input = sys.stdin.readline


N = int(input())

queue = deque([])

for i in range(1, N+1):
    queue.append(i)
    

paper = [0] + list(map(int, input().split()))
ball = []

for _ in range(N):
    num = queue.popleft()
    ball.append(num)
    if paper[num] > 0:
        jump = paper[num] -1
    else :
        jump = paper[num]
    queue.rotate(-jump)


print(' '.join(map(str,ball)))



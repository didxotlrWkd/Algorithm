import sys
from collections import deque

input = sys.stdin.readline

M , N = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])

result = 0

for x in range(N):
    for y in range(M):
        if tomatoes[x][y] == 1:
            queue.append([x,y])

def bfs():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while queue:
        x , y = queue.popleft()    
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M  and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append([nx,ny])                

bfs()


for tomatos in tomatoes:
    for tomato in tomatos:
        if tomato == 0:
            print(-1)
            exit(0)
    result = max(result , max(tomatos))

print(result - 1)        
        
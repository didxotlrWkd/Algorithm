import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
        
apart_gruop = 0
apart_count = []
visited = set()
def bfs():
    queue = deque()
    
    global apart_gruop
    
    dx = [-1, 1 ,0 ,0]
    dy = [0, 0, -1, 1]
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and (i,j) not in visited:
                queue.append([i,j])
                visited.add((i,j))
                
                apart_gruop += 1
                count = 0
                while queue:
                    x, y = queue.popleft()
                    count += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and (nx,ny) not in visited:
                            queue.append([nx, ny])
                            visited.add((nx, ny))
                apart_count.append(count)
                            
        
        
bfs()
print(apart_gruop)
apart_count.sort()
for i in range(len(apart_count)):
    print(apart_count[i])



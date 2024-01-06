import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))

for _ in range(T):
    M, N, K = map(int, input().split()) 
    count = 0
    
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    for n in range(N):
        for m in range(M):
            if graph[n][m] == 1:
                count += 1
                bfs(n,m)
    
    print(count)
        

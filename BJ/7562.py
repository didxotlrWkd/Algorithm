import sys

input = sys.stdin.readline
from collections import deque

T = int(input())

dx = [-2, -1, -2 , -1 , 1, 2, 1, 2]
dy = [1, 2 , -1, -2 , 2 , 1 , -2 , -1]

def bfs(start_x , start_y , end_x, end_y, size):
    chess = [[-1] * size for _ in range(size)]
    chess[start_x][start_y] += 1
    queue = deque()
    queue.append([start_x, start_y])
    
    while queue:
        x , y = queue.popleft()
        if x == end_x and y == end_y:
            return chess[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if 0 <= nx < size and 0 <= ny < size and chess[nx][ny] == -1:
                queue.append([nx, ny])
                chess[nx][ny] = chess[x][y] + 1      

for _ in range(T):
    size = int(input())
    start_x , start_y = map(int, input().split())
    end_x , end_y = map(int, input().split())
    print(bfs(start_x , start_y , end_x , end_y , size))
    
    
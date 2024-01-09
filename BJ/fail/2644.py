import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

p1 , p2 = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = set()
count = 0
result = 0

m = int(input())

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(v):
    global count 
    global result 
    visited.add(v)
    
    if v == p2:
        result = count
        return
    
    count += 1
    
    for i in graph[v]:
        if i not in visited:
            dfs(i)
    
dfs(p1)

if result == 0:
    print(-1)
else:
    print(result)
    
import sys
from collections import deque

input = sys.stdin.readline

N ,M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a , b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

def bfs(start_node):
    queue = deque([start_node])
    visited = [-1] * (N+1)
    visited[start_node] = 0
    while queue:
        curr_node = queue.popleft()
        for node in graph[curr_node]:
            if visited[node] == -1:
                queue.append(node)
                visited[node] = visited[curr_node] + 1
    return(sum(visited))
   
kevin = []
for i in range(1, N+1):
    kevin.append(bfs(i))


print(kevin.index(min(kevin)) + 1)
    
    
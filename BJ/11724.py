import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
    if v not in graph:
        graph[v] = []
    graph[v].append(u)

def bfs():
    visited = set() 
    queue = deque()
    count = 0
    for i in range(1, N + 1):
        if i not in visited:
            queue.append(i)
            visited.add(i)
            
            while queue:
                curr_node = queue.popleft()
                if curr_node in graph:
                    for k in graph[curr_node]:
                        if k not in visited:
                            queue.append(k)
                            visited.add(k)

            count += 1
    return count

print(bfs())
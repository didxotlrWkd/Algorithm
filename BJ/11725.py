import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = {}
parent_node = [0] * 100001

for _ in range(N-1):
    n , m = map(int,input().split())
    if n not in graph:
        graph[n] = []
    if m not in graph:
        graph[m] = []
    graph[n].append(m)
    graph[m].append(n)
    

def bfs():
    queue = deque([1])
    visited = set([1])
    
    while queue:
        curr_node = queue.popleft()
        for k in graph[curr_node]:
            if k not in visited:
                queue.append(k)
                visited.add(k)
            else:
                parent_node[curr_node] = k
                
bfs()
for i in range(2, N+1):
    print(parent_node[i])
                

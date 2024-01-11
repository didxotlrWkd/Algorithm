import sys
from collections import deque
input = sys.stdin.readline


N , M , V = map(int,input().split())

graph = {}

for i in range(M):
    a , b = map(int,input().split())
    
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
        
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph.values():
    i.sort()
    
visited_dfs = set()
    
def dfs(node):
    
    if node not in visited_dfs:
        print(node, end=' ')
        visited_dfs.add(node)
        if node not in graph:
            return
        
        for neighbor in graph[node]:
            dfs(neighbor)
            
dfs(V)        
                 
def bfs(v):
    visited = set([v])
    queue = deque([v])
    
    while queue:
        
        curr_node = queue.popleft()
        print(curr_node, end=' ')
        if curr_node not in graph:
            return
        
        for i in graph[curr_node]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
                    
print('')               
 
bfs(V)

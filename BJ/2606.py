import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = {}

for _ in range(M):
    a , b = map(int, input().split())
    
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
        
    graph[a].append(b)
    graph[b].append(a)
    
visited = set()

count = 0


def dfs(node):
    global count
    if node not in visited:
        visited.add(node)
        count += 1
        if node not in graph:
            return
        
        for n in graph[node]:
            dfs(n)
            

dfs(1)

print(count-1)
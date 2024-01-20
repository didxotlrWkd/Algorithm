import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

friend_list = [[] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]

for _ in range(m):
    a , b = map(int,input().split())
    friend_list[a].append(b)
    friend_list[b].append(a)
    
def bfs(my):
    global invited
    count = 0
    queue = deque([my])
    visited = set([my])
    depth[my] = 1
    
    while queue:
        curr_node = queue.popleft()
        for a in friend_list[curr_node]:
            if a not in visited:
                queue.append(a)
                visited.add(a)
                depth[a] += depth[curr_node] + 1
        

bfs(1)

invited = 0

for i in depth:
    if 1 < i <= 3:
        invited+=1

print(invited)
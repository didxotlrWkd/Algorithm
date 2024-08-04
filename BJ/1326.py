import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
bridge = [0] + list(map(int, input().split()))
a , b = map(int, input().split())
visited = [-1] * (N+1)

def cross(a,b):
    queue = deque()
    queue.append(a)
    visited[a] = 0
    
    while queue:
            curr_node = queue.popleft()

            for i in range(curr_node, N + 1 , bridge[curr_node]):
                if visited[i] == -1:
                    queue.append(i)
                    visited[i] = visited[curr_node] + 1
                    if i == b:
                        return visited[i]        
     
            for i in range(curr_node, 0 , -bridge[curr_node]):
                if visited[i] == -1:
                    queue.append(i)
                    visited[i] = visited[curr_node] + 1
                    if i == b:
                        return visited[i]
    return -1          
                
print(cross(a,b))
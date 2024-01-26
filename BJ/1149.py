import sys

input = sys.stdin.readline

N = int(input())

color_cost = [0]

for _ in range(N):
    color_cost.append(list(map(int, input().split()))) 
   
for i in range(2,N+1):
    color_cost[i][0] += min(color_cost[i-1][1] , color_cost[i-1][2])
    color_cost[i][1] += min(color_cost[i-1][0] , color_cost[i-1][2])
    color_cost[i][2] += min(color_cost[i-1][0] , color_cost[i-1][1])
    
print(min(color_cost[N][0], color_cost[N][1] , color_cost[N][2]))
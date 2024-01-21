import sys

input = sys.stdin.readline

N , M , B = map(int, input().split())
land = []

for _ in range(N):
    input_line = map(int, input().split())
    land.extend(input_line)
    

result = float('inf')
total_cost = 0

for i in range(min(land), max(land)+1):
    block = B
    cost = 0
    for k in land:
        if k - i > 0:
            cost += 2 * (k - i)
            block += 1
        else:
            cost += abs(k-i)
            block -= abs(k-i)
            
    if block >= 0  and cost <= result:
        result = i
        total_cost = cost
 
 

print(total_cost , result)        

        
import sys

input = sys.stdin.readline

N = int(input())

room = []

for i in range(N):
    x, y = map(int, input().split())
    room.append([x,y])
    
room.sort(key= lambda x : (x[1],x[0]))


end_time = 0
count = 0
for start , end in room:
    if end_time <= start:
        end_time = end
        count += 1  
        
print(count)
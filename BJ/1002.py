import sys
import math

input = sys.stdin.readline

T = int(input())

for i in range (T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    minr = abs(r1 -r2)
    maxr = r1 + r2
    
    if(distance == 0 and r1 == r2):
        print(-1)
    elif minr == distance or maxr == distance:
        print(1)
    elif minr < distance < maxr:
        print(2)
    else:
        print(0)



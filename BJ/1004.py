import sys
import math

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    x1 , y1 , x2 , y2 = map(int, input().split())
    
    n  = int(input())
    
    count = 0

    for _ in range(n):
        cx, cy, cr = map(int, input().split())
        startPoint = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        endPoint = math.sqrt((x2 - cx) ** 2  + (y2 - cy) ** 2)
        
        if startPoint < cr and endPoint < cr:
            pass
        elif startPoint > cr and endPoint < cr:
            count += 1
        elif startPoint < cr and endPoint > cr:
            count += 1
            
    print(count)
        
        
        
        
    
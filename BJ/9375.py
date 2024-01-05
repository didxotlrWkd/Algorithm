import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    closet = {}
    for _ in range(n):
        clothes , type = map(str,input().split())
        if type in closet.keys():
            closet[type] += 1
        else:
            closet[type] = 1
        
    count_list = []
    for value in closet.values():  
        count_list.append(value)

    result = 1
    for i in count_list:
        result *= (i+1)
        
    result -= 1
    
    print(result)
            
            
    
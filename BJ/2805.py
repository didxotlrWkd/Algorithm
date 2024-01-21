import sys

input = sys.stdin.readline

N , M = map(int, input().split())

trees = list(map(int, input().split()))

min_height = 1
max_height = max(trees)

while min_height <= max_height:
    cutted_tree = 0 
    mid_height = (max_height + min_height) // 2
    for tree in trees:
        if tree > mid_height:
            cutted_tree += tree - mid_height
            
    if cutted_tree >= M:  
        min_height = mid_height + 1
    else:
        max_height = mid_height - 1
    
print(max_height)
        
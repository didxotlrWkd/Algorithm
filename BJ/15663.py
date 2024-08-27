import sys

input = sys.stdin.readline

N , M = map(int, input().split())

numbers = sorted(list(map(int, input().split())))

per = []
visited = [False] * N

def back():
    if len(per) == M:
        print(' '.join(map(str, per)))
        return
    
    pre = 0
    
    for i in range(N):
        if not visited[i] and pre != numbers[i]:
            per.append(numbers[i])
            visited[i] = True
            pre = numbers[i]
            back()
            per.pop()
            visited[i] = False
     
    
back()

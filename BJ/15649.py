import sys

input = sys.stdin.readline

N , M = map(int,input().split())

seq = []

def back():
    if len(seq) == M:
        print(' '.join(map(str,seq)))
        return
  
    for i in range(1, N+1):
        if i not in seq:
            seq.append(i)
            back()
            seq.pop()
                
                
                
back()


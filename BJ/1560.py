import sys 

input = sys.stdin.readline

N = int(input())

if(N <= 2):
    print(N)
else:
    print(N + (N-2))
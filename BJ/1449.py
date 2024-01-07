import sys

input = sys.stdin.readline

N , L = map(int,input().split())

crack = list(map(int,input().split()))
count = 0
pipe = [0] * 2000 #1001하면 인덱스 에러 발생 왜그런지는 모름

for i in range(N):
    pipe[crack[i]] = 1
    
for k in range(len(pipe)):
    if pipe[k] == 1:
        for j in range(L):
            pipe[k+j] = 0
        count += 1
        
        
print(count) 
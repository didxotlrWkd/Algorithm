import sys

input = sys.stdin.readline


n = int(input())

wine = [int(input().strip()) for _ in range(n)]

dp = [0] * 10000

if n == 1:
    print(wine[0])
    exit()
    
if n == 2:
    print(wine[0] + wine[1])
    exit()

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0] + wine[2] , wine[1] + wine[2])

for i in range(3,n):
    dp[i] = max(dp[i-3] + wine[i-1] , dp[i-2], dp[i-4] + wine[i-1]) + wine[i]
    
print(max(dp))
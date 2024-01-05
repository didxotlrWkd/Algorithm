import sys

input = sys.stdin.readline

T = int(input())

def feb(num):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4,num+1):
        dp[i] = dp[i-3] + dp[i-2]
        
    print(dp[num])
    
for _ in range(T):
    N = int(input())
    feb(N)
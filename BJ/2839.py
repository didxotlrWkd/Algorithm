import sys

input = sys.stdin.readline

N = int(input())

dp = [-1] * 5001
dp[3] = 1
dp[5] = 1

def cal_min(n):
    if dp[n-3] == -1 and dp[n-5] == -1:
        return -1
    elif dp[n-3] == -1:
        return dp[n-5] + 1
    elif dp[n-5] == -1:
        return dp[n-3] + 1
    else:
        return min(dp[n-3]+1 , dp[n-5]+1)

for i in range(6,N+1):
    dp[i] = cal_min(i)
    
    
print(dp[N])
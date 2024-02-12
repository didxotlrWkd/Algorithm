import sys

input = sys.stdin.readline

N = int(input())

T = list()
P = list()

for _ in range(N):
    t1 , p1 =  map(int, input().split())
    T.append(t1)
    P.append(p1)

dp = [0] * (N+1)

for i in range(N):
    for j in range(i + T[i], N+1):
        dp[j] = max(dp[j] , dp[i] + P[i])


print(dp[N])
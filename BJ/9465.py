# import sys

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     sticker = [list(map(int, input().split())) for _ in range(2)]
#     score = 0
#     for i in range(2*n):
#         row = i // (n)
#         col = i % (n)
#         if row == 0:
#             if col == 0:
#                 if(sticker[row][col] >= sticker[row+1][col] + sticker[row][col+1]):
#                     score += sticker[row][col]
#                     sticker[row+1][col] = 0
#                     sticker[row][col+1] = 0
#                 else:
#                     sticker[row][col] = 0
#             elif col == (n-1):
#                 if(sticker[row][col] >= sticker[row][col-1] + sticker[row+1][col]):
#                     score += sticker[row][col]
#                     sticker[row][col-1] = 0
#                     sticker[row+1][col] = 0
#                 else:
#                     sticker[row][col] = 0
#             else:
#                 if(sticker[row][col]) >= sticker[row][col-1] + sticker[row][col+1] + sticker[row+1][col]:
#                     score += sticker[row][col]
#                     sticker[row][col-1] = 0
#                     sticker[row][col+1] = 0
#                     sticker[row+1][col] = 0
#                 else : 
#                     sticker[row][col] = 0
#         else:
#             if col == 0:
#                 if(sticker[row][col] >= sticker[row-1][col] + sticker[row][col+1]):
#                     score += sticker[row][col]
#                     sticker[row-1][col] = 0
#                     sticker[row][col+1] = 0
#                 else:
#                     sticker[row][col] = 0
#             elif col == (n-1):
#                 if(sticker[row][col] >= sticker[row][col-1] + sticker[row-1][col]):
#                     score += sticker[row][col]
#                     sticker[row][col-1] = 0
#                     sticker[row-1][col] = 0
#                 else:
#                     sticker[row][col] = 0
#             else:
#                 if(sticker[row][col]) >= sticker[row][col-1] + sticker[row][col+1] + sticker[row-1][col]:
#                     score += sticker[row][col]
#                     sticker[row][col-1] = 0
#                     sticker[row][col+1] = 0
#                     sticker[row-1][col] = 0
#                 else : 
#                     sticker[row][col] = 0
                    
#     print(score)

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1] + sticker[0][i], dp[0][i-1])
        dp[1][i] = max(dp[0][i-1] + sticker[1][i], dp[1][i-1])
        print(dp)

    print(max(dp[0][n-1], dp[1][n-1]))

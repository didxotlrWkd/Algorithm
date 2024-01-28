import sys
from collections import deque

input = sys.stdin.readline

#시간초과
# words = list(input().strip())

# order_num = int(input())

# cursor = len(words) 
# order_list = []

# for _ in range(order_num):
#     order = input().split()
#     if order[0] == 'L' and cursor > 0:
#         cursor -= 1
#     elif order[0] == 'D' and cursor < len(words):
#         cursor += 1
#     elif order[0] == 'B' and cursor > 0:
#         words = words[0:cursor-1] + words[cursor: ]
#         if cursor > 0:
#             cursor -= 1
#     elif order[0] == 'P':
#         words.insert(cursor, order[1])
#         cursor += 1
        
# for word in words:
#     print(word, end='')


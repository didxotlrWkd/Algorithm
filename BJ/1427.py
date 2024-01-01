import sys

input = sys.stdin.readline


num = list(input().strip())

num.sort(reverse=True)

print(''.join(num))
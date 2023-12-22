import sys

input = sys.stdin.readline

T = int(input())

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m-n))
    print(bridge)
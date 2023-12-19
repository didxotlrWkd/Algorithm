import sys

input = sys.stdin.readline

n, m =  map(int, input().split())

devideMoney = n // m
restMoney = n % m

print(devideMoney)
print(restMoney)


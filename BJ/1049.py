import sys

input = sys.stdin.readline

N , M = map(int , input().split())

set_string = []
each_string = []

for _ in range(M):
    set_price , each_price = map(int, input().split())
    set_string.append(set_price)
    each_string.append(each_price)
    
set_cheapest = min(set_string)
each_cheapest = min(each_string)

full_sets = N // 6
remaining = N % 6

price = min(full_sets * set_cheapest, full_sets * 6 * each_cheapest) + min(remaining * each_cheapest, set_cheapest)


print(price)
    
import sys

input = sys.stdin.readline

K, N = map(int, input().split())
wlans = []

for _ in range(K):
    wlans.append(int(input()))

start = 1
end = max(wlans)


while start <= end:
    count  = 0
    middle = (start + end) // 2

    for wlan in wlans:
        count += wlan // middle
        
    if count < N:
        end = middle - 1
        middle = (start + end) // 2
    else:
        start = middle + 1
        middle = (start + end) // 2
    

print(end)


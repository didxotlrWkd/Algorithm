import sys
import itertools

input = sys.stdin.readline

while True:
    picks = list(map(int, input().split()))
    if picks[0] == 0:
        break
    setted_picks = sorted(set(picks[1:]))
    pick_6 = itertools.combinations(setted_picks , 6)
    for arr in pick_6:
        for num in arr:
            print(num, end=" ")
        print("")
        
    print()
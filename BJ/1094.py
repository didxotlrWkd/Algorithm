import sys


input = sys.stdin.readline

X = int(input())

stick = [64,32,16,8,4,2,1]

count = 0

while(X!=0):
    for number in stick:
        if X >= number:
            X -= number
            count += 1
            break


print(count)


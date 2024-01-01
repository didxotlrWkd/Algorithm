import sys

input = sys.stdin.readline

N = int(input())


i = '666'
count = 0
num = 0
name = 0

while True:
    num += 1
    if i in str(num):
        count+=1
        name = num
    
    if count == N:
        break


print(name)
import sys

imput = sys.stdin.readline

X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    son = X
    mother = line - X + 1
else:
    son = line - X + 1
    mother = X


print(f"{son}/{mother}")

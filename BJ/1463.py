import sys

input = sys.stdin.readline

N = int(input())

def make_one(x):
    if x % 3 != 0 or x % 2 != 0:
        x -= 1
    
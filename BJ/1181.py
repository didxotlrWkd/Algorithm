import sys

input = sys.stdin.readline

N = int(input())

sorting_word = [input().strip() for _ in range(N)]

setted_words = list(set(sorting_word))
setted_words.sort()
setted_words.sort(key=len)

for word in setted_words:
    print(word)
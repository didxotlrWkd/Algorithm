
import sys

input = sys.stdin.readline

#한 줄을 읽어서 정수로 반환

number = int(input())

#한 줄을 읽고 공백으로 구분된 정수 입력받기

numbers = list(map(int, input().split()))

Num , ber = map(int, input().split())

#k행으로 이뤄진 2차월 배열 입력받기

k = 3

two_dimensional_array = [list(map(int, input().split())) for _ in range(k)]

#k개의 문자열들을 입력받기

words = [input().strip() for _ in range(k)]

#N행의 입력값을 1차원 리스트에 저장
N  = map(int, input().split())
land = []

for _ in range(N):
    input_line = map(int, input().split())
    land.extend(input_line)

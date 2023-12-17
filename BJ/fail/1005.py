import sys
 
input = sys.stdin.readline
 
 
T = int(input())

N, K = map(int, input().split())

building_time = [0] + list(map(int, input().split()))

print(building_time)

#정렬 알고리즘 부재
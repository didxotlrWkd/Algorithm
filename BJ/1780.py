import sys

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
plus = 0

def paper_count(row, col, n):
    global minus, zero, plus
    base = graph[row][col]
    
    for j in range(row, row+n):
        for k in range(col, col+ n):
            if graph[j][k] != base:
                devided_n = n//3
                paper_count(row, col, devided_n)
                paper_count(row, col + devided_n , devided_n)
                paper_count(row , col + (devided_n * 2) , devided_n)
                paper_count(row+devided_n , col, devided_n)
                paper_count(row+(devided_n*2) , col, devided_n)
                paper_count(row + devided_n , col+ devided_n , devided_n)
                paper_count(row + devided_n , col+ (devided_n*2), devided_n)
                paper_count(row+(devided_n*2) , col+devided_n , devided_n)
                paper_count(row+ (devided_n*2) , col+(devided_n*2) , devided_n)
                return 
            
    if base == 1:
        plus += 1
    elif base == 0:
        zero += 1
    else:
        minus += 1                    

paper_count(0,0,N)
print(minus)
print(zero)
print(plus)
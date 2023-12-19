# import sys

# input = sys.stdin.readline()

N = int(input())
number= N
cycle = 0

while True:
   num1 = number // 10
   num2 = number % 10
   result = (num1+ num2) % 10
   number = num2 * 10 + result
   cycle += 1
   
   if number == N:
       print(cycle)
       break
import sys

input = sys.stdin.readline

prime_list = [0] * 123457 * 2

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(len(prime_list)):
    if is_prime(i):
        prime_list[i] = 1

while True:
    num = int(input())
    if num == 0:
        break
    print(sum(prime_list[num+1:num*2 + 1])) 
    
    
    
    
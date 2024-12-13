import sys

input = sys.stdin.readline

switch_num = int(input())

switch = list(map(int, input().split()))

student_num = int(input())

student = []

def change(idx):
    if(switch[idx] == 0):
        switch[idx] = 1
    else:
        switch[idx] = 0

def change_man(num):
    for i in range(len(switch)):
        if((i + 1) % num == 0):
           change(i)
            
def change_woman(num):
    change(num-1)
    for i in range(1, (len(switch)//2) + 1):
        if num - 1 - i < 0:
            break
        if num - 1 + i >= len(switch):
            break
        if(switch[num-1-i] == switch[num-1+i]):
            change(num-1-i)
            change(num-1+i)
        else:
            break

for _ in range(student_num):
    sex , num = map(int, input().split())
    
    if sex == 1:
        change_man(num)
    else:
        change_woman(num)
             
                    
                    
for i in range(0, len(switch), 20):
    print(*switch[i:i+20], end=' ')
    print()
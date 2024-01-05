import sys
from collections import Counter

input = sys.stdin.readline

name = list(input().rstrip())
name.sort()
name_count = Counter(name)
count = 0
middle_name = ''
convert_name = ''


for key , value in name_count.items():
    if value % 2 == 1:
        count += 1
        middle_name = key
    
    if count > 1:
        print("I'm Sorry Hansoo")
        exit()
        
for key , value in name_count.items():
    convert_name += key * (value//2)
    

result = convert_name + middle_name + convert_name[::-1]
print(result)

import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input().strip()) for _ in range(N)]

nums.sort()

mean = round((sum(nums)/N))
print(mean)

middle = nums[(N//2)]
print(middle)

fre = {}

for i in nums:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1

max_fre = max(fre.values())
fres = []
fre_num = 0
for key,value in fre.items():
    if value == max_fre:
        fres.append(key)

if len(fres) > 1:
    fre_num = fres[1]
else:
    fre_num = fres[0]

print(fre_num)


range = max(nums) - min(nums)
print(range)




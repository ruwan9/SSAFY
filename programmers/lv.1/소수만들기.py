nums = [1,2,7, 6, 4]

def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

sum_num = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            sum_num.append(nums[i]+nums[j]+nums[k])

sum_num = list(set(sum_num))

cnt = 0
for num in sum_num:
    if is_prime(num):
        cnt += 1
    
print(cnt)



# 2
from itertools import combinations

def is_prime(a, b, c):
    tot = a+b+c
    for i in range(2, tot):
        if tot % i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    lst = list(combinations(nums, 3))
    for i in lst:
        if is_prime(i[0], i[1], i[2]):
            cnt += 1
    return cnt

print(solution(nums))
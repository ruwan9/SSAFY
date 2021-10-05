import sys
sys.stdin = open('2920_input.txt')

#################### 방법 1 ####################
# def discrimination(numbers):
#     if numbers == sorted(numbers):
#         return 'ascending'

#     elif numbers == sorted(numbers, reverse=True):
#         return 'descending'

#     else:
#         return 'mixed'


# numbers = list(map(int, input().split()))
# print(discrimination(numbers))

#################### 방법 2 ####################
a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')


"""
1. 리스트에서 원소를 차례대로 비교
2. 비교 시 두 원소를 기준으로 오름차순/내림차순 여부 체크
"""

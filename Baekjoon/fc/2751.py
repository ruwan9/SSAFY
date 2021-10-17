import sys
sys.stdin = open('input_files/2751.txt')

# # python 사용 시 시간초과 - pypy3는 통과
# N = int(input())
# numbers = sorted(list(int(input()) for _ in range(N)))
# for number in numbers:
#     print(number)
#

# 병합 정렬
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i]< right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i ==  len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)

"""
데이터 개수가 최대 1,000,000개 -> 시간복잡도 O(NlogN) 알고리즘 필요
- NlogN 사용 시 20,000,000정도 가능 (파이썬은 1초에 2천만번정도 연산 가능)

"""
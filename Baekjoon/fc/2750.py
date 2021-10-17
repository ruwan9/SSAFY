import sys
sys.stdin = open('input_files/2750.txt')

#################### sorted ####################
# N = int(input())
# numbers = sorted(list(int(input()) for _ in range(N)))
#
# for i in numbers:
#     print(i)

#################### 선택정렬 ####################
N = int(input())
array = list(int(input()) for _ in range(N))

for i in range(N):
    min_idx = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, N):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]  # 스와프

for i in array:
    print(i)
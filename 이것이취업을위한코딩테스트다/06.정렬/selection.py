# 선택정렬

#################### 방법 1 ####################
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = array.index(min(array[i:]))  # 최소값의 index를 min_idx에 저장

    if array[i] >= array[min_idx]:  # 맨 앞의 값과 비교해서
        array[i], array[min_idx] = array[min_idx], array[i]  # swap

print(array)

#################### 방법 2 ####################
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 index
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # swap

print(array)

"""
선택정렬
1. 가장 작은 데이터를 선택해 맨 앞의 데이터와 swap
2. 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 swap
3. 반복

시간복잡도: O(N^2)
"""
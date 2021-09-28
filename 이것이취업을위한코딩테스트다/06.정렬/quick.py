# 퀵 정렬

#################### 방법 1 ####################
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):  # start, end는 index값임
    if start >= end:  # 원소가 1개인 경우 종료
        return

    pivot = start  # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터 찾을때까지 반복 - left
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터 찾을때까지 반복 - right
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈린 경우 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 큰 데이터와 작은 데이터 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽과 오른쪽, 각각 정렬
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)


#################### 방법 2 ####################
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 왼쪽 분할
    right_side = [x for x in tail if x > pivot]  # 오른쪽 분할

    # 분할 이후 왼쪽과 오른쪽 각각 정렬, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

"""
퀵 정렬
1. 기준 데이터 설정
2. 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸기
3. 피벗을 기준으로 왼쪽/오른쪽 리스트에서 각각 정렬을 다시 수행

피벗 (Pivot)
- 교환하기 위한 '기준'

호어 분할 방식 (Hoare Partition)
- 리스트에서 첫 번째 데이터를 피벗으로 정한다.

시간복잡도: O(NlogN)
"""
arr = [4, 3, 2, 1]

# 1
def solution(arr):
    arr.pop(arr.index(min(arr)))  # 가장 작은 수의 index를 찾아 arr에서 빼내기(pop)

    if arr == []:
        return [-1]
    else:
        return arr
print(solution(arr))

# 2
def rm_small(lst):
    return [i for i in lst if i > min(lst)]

print(rm_small(arr))
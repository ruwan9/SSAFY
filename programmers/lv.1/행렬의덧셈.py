arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

# 1
def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    arr = [[] for _ in range(n)]  # arr = [[], []]

    for i in range(n):
        for j in range(m):
            arr[i].append(arr1[i][j] + arr2[i][j])
    return arr
print(solution(arr1, arr2))

# 2
def solution2(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1
print(solution2(arr1, arr2))

arr = [1, 2, 3, 4]

# 1
def solution(arr):
    sum_arr = 0

    for i in arr:
        sum_arr += i

    return sum_arr / len(arr)

print(solution(arr))

# 2
def solution2(arr):
    try:
        return sum(arr) / len(arr)
    except ZeroDivisionError:
        return 0

print(solution2(arr))
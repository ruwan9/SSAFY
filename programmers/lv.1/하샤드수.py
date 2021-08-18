arr = 11

# 1
def solution(arr):
    arr_lst = list(str(arr))
    arr_sum = 0

    for i in arr_lst:
        arr_sum += int(i)
    
    if arr % arr_sum:
        return False
    return True

print(solution(arr))

# 2
def harchad(n):
    return n % sum([int(i) for i in str(n)]) == 0  # 나누어 떨어지면 True

print(harchad(arr))
arr = [5, 9, 7, 10]	
divisor = 5

# arr = [3, 2, 6]	
# divisor = 10

def solution(arr, divisor):
    lst = []
    for element in arr:
        if not element % divisor:
            lst.append(element)
    if lst:
        return sorted(lst)
    return [-1]
print(solution(arr, divisor))


# 2
def solution2(arr, divisor):
    ans = [num for num in arr if num % divisor == 0]

    if ans:  # element가 하나라도 있는 경우
        return sorted(ans)
    return [-1]

print(solution2(arr, divisor))
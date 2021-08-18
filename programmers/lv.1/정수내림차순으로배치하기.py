n = 118372

# 1
def solution(n):
    lst = list(str(n))  # list로 만들고
    lst.sort(reverse=True)  # 내림차순 정렬
    return int(''.join(lst))  # 정수로 return

print(solution(n))

# 2
def solution2(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))

print(solution2(n))
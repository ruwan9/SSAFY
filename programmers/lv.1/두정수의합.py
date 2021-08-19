a = 3
b = 5

def solution(a, b):
    if a > b:  # a, b 서로 바꿔주기
        (a, b) = (b, a)
    ans = 0
    if a == b:
        ans = a
    else:
        ans = 0
        for i in range(a, b+1):
            ans += i
    return ans
print(solution(a, b))

# 2
def solution2(a, b):
    if a>b:
        return sum(list(range(b, a+1)))
    else:
        return sum(list(range(a, b+1)))
print(solution2(a, b))
n = 4

# 1.
def solution(n):
    if n % 2:
        return '수박' * (n//2) + '수'
    else:
        return '수박' * (n//2)
print(solution(n))

# 2.
def solution2(n):
    ans = ''
    for i in range(n):
        if i % 2:
            ans += '박'
        else:
            ans += '수'
    return ans
print(solution2(n))
from typing import AnyStr


N = 123

# 1.
def solution(n):
    ans = 0
    for i in str(n):
        ans += int(i)
    return ans
print(solution(N))

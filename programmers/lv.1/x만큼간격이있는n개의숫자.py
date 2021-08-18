x = 2
n = 5

# 1
def solution(x, n):
    ans = []
    for i in range(1, n+1):
        ans.append(x*i)
    return ans
print(solution(x, n))

# 2
def solution2(x, n):
    return [x*i + x for i in range(n)]
print(solution2(x, n))
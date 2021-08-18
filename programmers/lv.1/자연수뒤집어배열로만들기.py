n = 1048204

# 1 ... 이건 왜 안될까???
def solution(n):
    return [int(i) for i in sorted(list(str(n)), reverse=True)]
print(solution(n))

# 2.
def solution2(n):
    lst = list(str(n))
    ans = []
    for i in lst:
        ans.append(int(i))
    ans.reverse()

    return ans
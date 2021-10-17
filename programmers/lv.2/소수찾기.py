numbers	= "011"


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def dfs(idx, tmp):
    if tmp != '':
        lst.add(int(tmp))
    if idx == N:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            new_tmp = tmp + numbers[i]
            dfs(idx+1, new_tmp)
            visited[i] = 0


N = len(numbers)
subset = []
visited = [0] * N
lst = set()


dfs(0, '')

cnt = 0
for i in lst:
    if is_prime(i):
        cnt += 1

print(cnt)




#################### 방법 1. ####################
numbers	= "011"


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def dfs(idx, tmp, N, visited, numbers, lst):
    if tmp != '':
        lst.add(int(tmp))
    if idx == N:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            new_tmp = tmp + numbers[i]
            dfs(idx + 1, new_tmp, N, visited, numbers, lst)
            visited[i] = 0


def solution(numbers):
    N = len(numbers)
    visited = [0] * N
    lst = set()
    dfs(0, '', N, visited, numbers, lst)
    lst = list(lst)
    cnt = 0
    for i in lst:
        if is_prime(i):
            cnt += 1

    return cnt


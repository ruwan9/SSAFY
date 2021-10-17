numbers = [1, 1, 1, 1, 1]
target = 3
N = len(numbers)
cnt = 0


def dfs(idx, tmp):
    global cnt
    if idx == N:
        if tmp == target:
            cnt += 1
        return

    dfs(idx+1, tmp+numbers[idx])  # 더하기
    dfs(idx+1, tmp-numbers[idx])  # 빼기


dfs(0, 0)
print(cnt)
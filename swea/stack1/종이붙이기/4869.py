#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())//10

    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, N+1):
        # 규칙 f(n) = f(n-1) + 2*f(n-2)
        dp[i] = dp[i-1] + 2*dp[i-2]

    print(f'#{tc}', dp[-1])


#################### 방법 2. ####################
# 재귀
import sys
sys.stdin = open('input.txt')


def dp(n):
    if n < 2:
        return 1
    return dp(n-1) + dp(n-2) * 2


for t in range(1, int(input())+1):
    n = int(input())
    print(f'#{t} {dp(n//10)}')

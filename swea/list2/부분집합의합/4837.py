#################### 방법 1. ####################
# 부분집합 구할 때 itertools의 combinations 사용
import sys
sys.stdin = open('input.txt')

from itertools import combinations  # 조합

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    combs = list(combinations(range(1, 13), N))  # 1부터 12까지의 숫자 중 N개를 뽑아 만들 수 있는 조합들
    for comb in combs:
        if sum(comb) == K:
            cnt += 1

    print(f'#{tc} {cnt}')



#################### 방법 2. ####################
# 비트연산자 이용
import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    a = [i for i in range(1, 13)]
    result = 0

    for i in range(1 << 12):
        cnt = 0
        total = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                total += a[j]
        if cnt == n and total == k:
            result += 1

    print(f'#{t} {result}')
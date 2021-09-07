import sys
sys.stdin = open('11047_input.txt')

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

sorted_coins = sorted(coins, reverse=True)

cnt = 0
for coin in sorted_coins:
    cnt += K//coin
    K %= coin

    if K == 0:
        break

print(cnt)

"""
가장 큰 단위가 항상 작은 단위의 배수일 때만 위와 같은 for문 사용 가능
-> 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문

중간에 K가 0이 되면 그 이상의 불필요한 연산을 막도록 break 추가
"""
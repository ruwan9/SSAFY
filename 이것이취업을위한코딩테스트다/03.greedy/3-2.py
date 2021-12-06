#################### 방법 1. ####################
import sys
sys.stdin = open('input3-2.txt')

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers = sorted(numbers, reverse=True)  # 내림차순으로 정렬

tot = 0
while True:
    for i in range(K):
        if M == 0:
            break
        tot += numbers[0]  # 가장 큰 수를 K번 더하기
        M -= 1
    
    if M == 0:
        break
    tot += numbers[1]  # 두번째로 큰 수 한 번 더하기
    M -= 1

print(tot)

"""
1. 가장 큰 수를 K번 더하고
2. 두번째로 큰 수를 한 번 더하기
반복
"""

#################### 방법 2. ####################
import sys
sys.stdin = open('input3-2.txt')

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수
count = (M // (K+1)) * K
count += M % (K+1)

result = 0
result += count * first  # 가장 큰 수 더하기
result += (M-count) * second  # 두 번째로 큰 수 더하기

print(result)

"""
1. 반복되는 수열 파악
    -> 길이는 K+1
2. 반복되는 횟수 파악
    -> 횟수는 M // (K+1)

3. 가장 큰 수가 등장하는 횟수
    -> (M // (K+1)) * K + M % (K+1)  # 나누어 떨어지지 않을 때
"""


#################### 방법 3. ####################
import sys
sys.stdin = open('input3-2.txt')

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
# 정렬
data.sort()

ans = 0
while M > K:
    ans += data[-1] * K + data[-2]  # 가장 큰 수 K번 더하고 두 번째 큰 수 한 번 더하기
    M -= (K+1)  # M에서 K+1 빼주기
ans += data[-1] * M  # 남는 수만큼 가장 큰 수 더해주기

print(ans)
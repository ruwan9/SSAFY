import sys
sys.stdin = open('input_files/2798.txt')

#################### 방법 1 ####################
# N, M = map(int, input().split())
# cards = list(map(int, input().split()))

# # nCr 조합
# scores = []
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             if cards[i]+cards[j]+cards[k] <= M:
#                 scores.append(cards[i]+cards[j]+cards[k])
# scores.sort()
# print(scores[-1])

#################### 방법 1 ####################
n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0
length = len(data)

count = 0
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)  # 가장 큰 값

print(result)
"""
1. 카드 3개 뽑는 경우의 수 = nC3 (조합) __ n(n-1)(n-2)/3! 개의 경우의 수
2. 3중 반복문 사용
"""

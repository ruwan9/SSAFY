import sys
sys.stdin = open('input_files/12865.txt')


# N, K = map(int, input().split())
# dp = [[0] * (K+1) for _ in range(N+1)]
# print(dp)
# for i in range(1, N+1):
#     W, V = map(int, input().split())
#     for j in range(1, K+1):
#         if W > j:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V)
# print(dp)

"""
point: 모든 무게에 대하여 최대 가치를 정하기
- d[i][j] = 배낭에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치
- 각 물품의 번호 i에 따라 최대 가치 테이블 d[i][j]를 갱신하여 문제 해결
"""

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)
print(dp[N][K])
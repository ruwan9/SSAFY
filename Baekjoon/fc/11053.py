import sys
sys.stdin = open('input_files/11053.txt')

# N = int(input())
# data = sorted(list(set(list(map(int, input().split())))))
# print(len(data))

N = int(input())
data = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
import sys
sys.stdin = open('2304_input.txt')

N = int(input())

poles = [list(map(int, input().split())) for _ in range(N)]

poles.sort()
print(poles)

heights = [poles[i][1] for i in range(N)]
print(heights)

max_idx = heights.index(max(heights))  # 최고 높이 구하기
print(max_idx)


for i in range(1, max_idx+1):  # 최고 높이 전
    if poles[i-1][1] > poles[i][1]:
        poles[i][1] = poles[i-1][1]
print(poles)

for i in range(N-1, max_idx, -1):  # 최고 높이 후
    if poles[i-1][1] < poles[i][1]:
        poles[i-1][1] = poles[i][1]
print(poles)

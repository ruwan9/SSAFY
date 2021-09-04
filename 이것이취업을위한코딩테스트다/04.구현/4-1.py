import sys
sys.stdin = open('input1.txt')

N = int(input())
plans = input().split()
print(plans)

x, y = 1, 1  # 시작지점

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

compass = ['U', 'D', 'L', 'R']  # 움직이는 방향

for plan in plans:
    for i in range(len(compass)):
        if plan == compass[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > N or ny > N:  # 공간을 넘어가는 경우 무시
        continue

    x = nx
    y = ny

print(x, y)
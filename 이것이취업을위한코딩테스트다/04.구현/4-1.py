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

"""
'시뮬레이션'

1. 이동 방향을 dx, dy 리스트로 만들어두고
2. 움직이는 방향에 따라 초기 시작 x, y값에 추가하여 이동 후 좌표를 구해준다.

공간을 넘어가는 경우 무시하는 것도 잊지 말기 
"""
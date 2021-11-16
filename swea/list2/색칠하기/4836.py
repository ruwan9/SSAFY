#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = []
    for _ in range(N):
        square = list(map(int, input().split()))
        data.append(square)


    # 10*10 격자
    background = list([0] * 10 for _ in range(10))
    # 빨강은 1, 파랑은 2

    for lst in data:
        if lst[-1] == 1:
            # 빨간색 칠하는 영역
            for r in range(lst[0], lst[2]+1):
                for c in range(lst[1], lst[3]+1):
                    if background[r][c] != 1:
                        background[r][c] += 1

        if lst[-1] == 2:
            #파란색 칠하는 영역
            for r in range(lst[0], lst[2]+1):
                for c in range(lst[1], lst[3]+1):
                    if background[r][c] != 2:
                        background[r][c] += 2

    ans = 0
    for r in range(10):
        for c in range(10):
            if background[r][c] == 3:  # 보라색이 된 칸의 수(빨강 1 + 파랑 2 = 보라 3)
                ans += 1

    print(f'#{tc} {ans}')

#################### 방법 2. ####################
# input 받을때마다 처리하여 정리
import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):  # 테스트 케이스
    arr = [[0]*10 for _ in range(10)]
    for n in range(int(input())):   # 색칠 영역
        r1, c1, r2, c2, color = map(int, input().split())

        # arr 에 색칠
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    result = 0
    for row in arr:  # arr 의 값이 3일 경우 보라색
        result += row.count(3)
    print(f'#{tc} {result}')

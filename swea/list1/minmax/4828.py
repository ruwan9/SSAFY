#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')

# min(), max() 사용
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    print(f'#{tc} {max(data) - min(data)}')


#################### 방법 2. ####################
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    # 초기화
    min_num = data[0]
    max_num = data[0]
    # 순회하며 최대, 최소값 갱신
    for num in data:
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num

    print(f'#{tc} {max_num - min_num}')
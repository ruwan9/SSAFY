# n, m = map(int, input().split())
n = 5  # 가로
m = 3  # 세로

# 1
for _ in range(m):
    print('*' * n)

# 2
for i in range(m):
    for j in range(n):
        print('*', end='')  # 옆에 추가
    print()  # 줄바꿈
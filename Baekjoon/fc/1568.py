import sys
sys.stdin = open('input_files/1568.txt')


N = int(input())

cnt = 0
birds = N  # 새의 수
i = 1  # 불러야하는 수

while birds != 0:

    if i <= birds:
        cnt += 1
        birds -= i
        i += 1
    else:
        i = 1

print(cnt)
# 불러야하는 수 - 남은 새의 수 - cnt
# 1 - 13 - 1
# 2 - 11 - 2
# 3 - 8 - 3
# 4 - 4 - 4
# 5 - x
# 1 - 3 - 5
# 2 - 1 - 6
# 3 - x
# 1 - 1 - 7
# 2 - 0


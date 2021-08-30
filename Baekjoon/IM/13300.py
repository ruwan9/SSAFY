import sys
sys.stdin = open('13300_input.txt')


def room_cnt(grades):
    cnt = 0
    for i in grades:
        if i % 2 == 0 and i != 0:
            cnt += i//2
        elif i % 2 != 0:
            cnt += i//2 + 1
    return cnt

N, K = map(int, input().split())
grades_m = [0]*7
grades_f = [0]*7
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        grades_f[Y] += 1
    elif S == 1:
        grades_m[Y] += 1

print(room_cnt(grades_f) + room_cnt(grades_m))
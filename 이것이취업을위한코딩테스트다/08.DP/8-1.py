import sys
sys.stdin = open('input1.txt')

X = int(input())
cnt = 0

# dp table
d = [0] * 100

# bottom-up
for i in range(2, X+1):
    # 1 빼는 경우
    d[i] = d[i-1] + 1
    # 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # 5로 나누어 떨어지는 경우
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[X])
"""
호출 횟수를 구하기 위해 +1 추가로 해주기
"""
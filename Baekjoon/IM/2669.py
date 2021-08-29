import sys
sys.stdin = open('2669_input.txt')

matrix = [[0]*101 for _ in range(101)]


for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1
ans = 0
for row in matrix:
    ans += sum(row)

print(ans)
#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(input() for _ in range(N))
    # print(data)

    # 가로 확인
    for word in data:
        for i in range(N-M+1):
            row = word[i:M+i]
            if row == row[::-1]:
                print(f'#{tc}', row)
    # 세로 확인
    for i in range(N-M+1):
        for j in range(N):
            col = []
            for k in range(M):
                col.append(data[i+k][j])

            if col == col[::-1]:
                print(f'#{tc} ', *col, sep='')

#################### 방법 2. ####################
import sys
sys.stdin = open('input.txt')


# check palindrome
def check(row):
    for i in range(len(row)//2):
        if row[i] != row[-i-1]:
            return False
    return True


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    arr2 = list(zip(*arr))  #Transpose

    for row, row2 in zip(arr, arr2):
        for i in range(N-M+1):
            if check(row[i:i+M+1]):
                print(f'#{test_case} ', *row[i:i+M+1], sep='')
            elif check(row2[i:i+M+1]):
                print(f'#{test_case} ', *row2[i:i+M+1], sep='')

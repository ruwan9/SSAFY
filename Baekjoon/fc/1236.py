import sys
sys.stdin = open('input_files/1236.txt')

# #################### 방법 1. ####################
# # 배열(arr) 중 'X'가 없는 열의 수만큼 return
# def check(arr):
#     cnt = 0
#     for i in arr:
#         if 'X' not in i:
#             cnt += 1
#     return cnt
#
# N, M = map(int, input().split())
# castle = [list(input()) for _ in range(N)]
#
# # 가로 확인
# r_cnt = 0
# r_cnt = check(castle)
#
# new_arr = []
# # 세로 확인
# # 세로 줄을 확인하기 위해 열 <=> 행 을 바구어 새로운 배열(new_arr)에 저징
# for col in range(M):
#     lst = []
#     for row in range(N):
#         lst.append(castle[row][col])
#     new_arr.append(lst)
#
# c_cnt = 0
# c_cnt = check(new_arr)
#
# print(max(r_cnt, c_cnt))


#################### 방법 2. ####################
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(input())
print(array)
row = [0] * n
col = [0] * m

# 행 기준, 열 기준 경비원이 존재하지 않는 위치에는 0, 존재하는 위치에는 1
for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':  # 경비원이 존재하는 위치
            row[i] = 1
            col[j] = 1
print(row)
print(col)
row_cnt = 0
for i in range(n):
    if row[i] == 0:  # 경비원이 존재하지 않는 경우
        row_cnt += 1

col_cnt = 0
for j in range(m):
    if col[j] == 0:
        col_cnt += 1

print(max(row_cnt, col_cnt))
"""
1. 행 기준, 열 기준 필요한 경비원 수를 계산
2. 더 큰 수를 출력
"""
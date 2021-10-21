import sys
sys.stdin = open('input_files/1668.txt')

# #################### 방법 1. ####################
N = int(input())
data = list(int(input()) for _ in range(N))

left_cnt = 1  # 왼쪽에서 보이는 개수
right_cnt = 1  # 오른쪽에서 보이는 개수

# 왼쪽부터
tmp = data[0]
for i in range(1, N):
    if tmp < data[i]:
        left_cnt += 1
        tmp = data[i]
print(left_cnt)

# 오른쪽부터
data.reverse()  # 오른쪽부터 보기 위해 .reverse() 해줌
tmp = data[0]
for i in range(1, N):
    if tmp < data[i]:
        right_cnt += 1
        tmp = data[i]
print(right_cnt)


# #################### 방법 2. ####################
# # tc는 다 맞는데 답은 틀림...
# N = int(input())
# data = list(int(input()) for _ in range(N))
# left_cnt = 1  # 왼쪽에서 보이는 개수
# right_cnt = 1  # 오른쪽에서 보이는 개수
#
# for i in range(1, N):
#     if data[i] == max(data):
#         left_cnt += 1
#     if data[i] < max(data[i:]) and data[i]> max(data[:i]):
#         left_cnt += 1
# print(left_cnt)
#
# data.reverse()
# for i in range(1, N):
#     if data[i] == max(data):
#         right_cnt += 1
#     if data[i] < max(data[i:]) and data[i]> max(data[:i]):
#         right_cnt += 1
# print(right_cnt)

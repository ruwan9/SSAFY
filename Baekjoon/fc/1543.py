import sys
sys.stdin = open('input_files/1543.txt')


#################### 방법 1. ####################
# 틀림

# doc = input()
# to_find = input()
# n = len(to_find)
#
# cnt = 0
# for j in range(len(doc)+1-n):
#     tmp = 0
#     for i in range(j, len(doc)+1-n):
#         if doc[i*n:i*n+n] == to_find:
#             tmp += 1
#
#     if cnt < tmp:
#         cnt = tmp
#
# print(cnt)


#################### 방법 2. ####################
doc = input()
to_find = input()
n = len(to_find)
cnt = 0
i = 0
while i <= len(doc)+1-n:
    if doc[i:i+n] == to_find:
        cnt += 1
        i += n
    else:
        i += 1

print(cnt)



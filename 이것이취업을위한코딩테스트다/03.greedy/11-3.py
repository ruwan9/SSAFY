import sys
sys.stdin = open('input11-3.txt')

#################### 방법 1 ####################
# data = input()
# temp = data[0]

# cnt = 0
# for i in data:
#     if i != temp:
#         temp = i
#         cnt += 1
# if cnt % 2 == 0:
#     print(cnt // 2)
# else:
#     print(cnt // 2 + 1)


#################### 방법 2 ####################
data = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 모든 원소를 확인
for i in range(len(data)-1): 
    if data[i] != data[i+1]:
        if data[i+1] == '1':  # 1로 바뀌는 경우
            count0 += 1
        else:  # 0으로 바뀌는 경우
            count1 += 1

print(min(count0, count1))

"""
1. 전부 0으로 바꾸는 경우
2. 전부 1로 바꾸는 경우
두 경우를 모두 계산해본 후 작은 값을 프린트
"""
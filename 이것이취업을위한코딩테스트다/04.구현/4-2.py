import sys
sys.stdin = open('input2.txt')

#################### 방법 1 ####################
N = int(input())

cnt = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                cnt += 1
print(cnt)


"""
'완전탐색'

1. 목표 시간, 60분, 60초의 시간을 문자열로 만들 1씩 증가시키기 (3중 for문)
2. 만들어진 문자열에 '3'이 들어가는 경우 cnt에 1 추가
"""



#################### 방법 2 ####################
# N = int(input())

# cnt = 0

# for hour in range(N+1):  # 0, 1, 2, 3, 4, 5
#     for minute in range(60):  # 0~59
#         for second in range(60):  # 0~59
#             if '3' in str(hour)+str(minute)+str(second):
#                 cnt += 1

# print(cnt)

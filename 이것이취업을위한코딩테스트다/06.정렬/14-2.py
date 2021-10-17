import sys
sys.stdin = open('input14-2.txt')

#################### 방법 1 ####################
# N = int(input())
# houses = list(map(int, input().split()))
# houses.sort()

# lengths = []
# # 안테나 위치에 따른 각 집 사이의 거리를 계산한 값을 length에 append
# for i in range(min(houses), max(houses)):
#     cnt = 0
#     for house in houses:
#         cnt += abs(i - house)
#     lengths.append(cnt)

# # 최소값의 집 위치 return
# print(lengths.index(min(lengths)) + 1)


#################### 방법 1 ####################
N = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(N-1) // 2])

"""
중간값(Median)에 해당하는 위치의 집에 안테나 설치 시 거리가 최소
1. 오름차순 정렬
2. 중간값 출력
"""
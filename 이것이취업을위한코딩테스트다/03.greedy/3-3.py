import sys
sys.stdin = open('input3.txt')

# 1. min값을 모은 list 활용
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

min_lst = []
for row in matrix:
    min_lst.append(min(row))

print(max(min_lst))


# 2. min() 함수 이용
N, M = map(int, input().split())
result = 0
for i in range(N):
    data = list(map(int, input().split()))

    min_value = min(data)
    result = max(min_value, result)

print(result)


# 3. 2중 반복문 구조 이용
N, M = map(int, input().split())
result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = 10001

    for j in data:
        min_value = min(min_value, j)
    
    result = max(result, min_value)

print(result)
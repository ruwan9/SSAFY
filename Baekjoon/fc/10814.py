import sys
sys.stdin = open('input_files/10814.txt')

#################### 방법 1 ####################
# N = int(input())
# data = list(list(map(str, input().split())) for _ in range(N))
#
# data = sorted(data, key=lambda x: int(x[0]))
# for i in data:
#     print(*i)

#################### 방법 2 ####################
N = int(input())
array = []
for _ in range(N):
    data = input().split(' ')
    array.append((int(data[0]), data[1]))

array = sorted(array, key=lambda x: x[0])

for i in array:
    print(*i)

"""
sorted만 해도 나머지는 들어온 순서대로 정렬해줌
"""
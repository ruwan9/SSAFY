import sys
sys.stdin = open('input2.txt')

#################### 방법 1 ####################
# N = int(input())
# info = []
# for _ in range(N):
# 	name, score = input().split()
# 	info.append((name, int(score)))

# info.sort()

# for i in info:
# 	print(i[0], end=' ')


#################### 방법 2 ####################
N = int(input())
array = []
for _ in range(N):
	name, score = input().split()
	array.append((name, int(score)))

# key를 이용, 점수 기준으로 정렬
array = sorted(array, key = lambda student: student[1])

for student in array:
	print(student[0], end=' ')
import sys
sys.stdin = open('input1.txt')

#################### 방법 1 ####################
N = int(input())
array = list(int(input()) for _ in range(N))
ans = sorted(array, reverse=True)

for i in ans:
	print(i, end=' ')

#################### 방법 2 ####################

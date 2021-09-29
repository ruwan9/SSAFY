import sys
sys.stdin = open('input12-1.txt')

#################### 방법 1 ####################
# score = input()
# left = 0
# for i in score[:len(score)//2]:
# 	left += int(i)

# right = 0
# for j in score[len(score)//2:]:
# 	right += int(j)

# if left == right:
# 	print('LUCKY')
# else:
# 	print('READY')


#################### 방법 2 ####################
N = input()
length = len(N)
summary = 0

for i in range(length // 2):
	summary += int(N[i])

for i in range(length // 2, length):
	summary -= int(N[i])

if summary == 0:
	print('LUCKY')
else:
	print('READY')
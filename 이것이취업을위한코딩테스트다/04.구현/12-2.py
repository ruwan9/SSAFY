import sys
sys.stdin = open('input12-2.txt')

#################### 방법 1 ####################
S = input()
lst = []
num = 0
for i in S:
	if i.isalpha():  # 알파벳인 경유
		lst.append(i)
	else:  # 숫자는 따로 더하기
		num += int(i)

# 알파벳 오름차순 정렬
lst.sort()
# 뒤에 숫자 더하기
if num != 0:
	lst.append(str(num))

# 문자열로 출력
print(''.join(lst))

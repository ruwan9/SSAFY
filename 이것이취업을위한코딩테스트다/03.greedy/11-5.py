import sys
sys.stdin = open('input11-5.txt')

#################### 방법 1 ####################
# N, M = map(int, input().split())
# weights = list(map(int, input().split()))
# weights.sort()
# print(weights)

# cnt = 0
# for i in range(N-1):
# 	for j in range(i+1, N):
# 		if weights[i] != weights[j]:
# 			cnt += 1
# print(cnt)


#################### 방법 1 ####################
N, M = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지 무게를 담을 수 있는 리스트
array = [0]*10

for x in data:
	# 각 무게에 해당하는 볼링공 개수 카운트
	array[x] += 1

res = 0
# 1부터 M가지 각 무게에 대하여
for i in range(1, M+1):
	N -= array[i]  # 무게가 i인 볼링공의 개수 제외
	res += array[i] * N  # B가 선택하는 경우의 수 곱하기

print(res)

"""
무게 별 볼링공 갯수 파악
1. A가 특정 무게의 볼링공 선택
2. B가 이어서 볼링공 선택

이미 계산한 경우는 제외 (조합)
"""
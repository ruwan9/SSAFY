import sys
sys.stdin = open('input11-4.txt')

N = int(input())
data = list(map(int, input().split()))
data.sort()  # 오름차순 정렬
print(data)

target = 1
for x in data:
	# 만들 수 없는 금액을 찾으면 반복 종료
	if target < x:
		break
	target += x

# 만들 수 없는 금액 출력
print(target)


"""
오름차순 정렬
ex) 1, 2, 3, 8의 화폐 단위일 경우
1부터 만들 수 있는 금액 확인 (target = 1)
가능하다면 target = 1 + 1 = 2로 업데이트
target = 2를 만족하는지 확인
가능하다면 target = 2 + 2 = 4로 업데이트
target = 4를 만족하는지 확인
가능하다면 target = 4 + 3 = 7로 업데이트
target = 7을 만족하는지 확인
없으므로 최대값 = 7
"""

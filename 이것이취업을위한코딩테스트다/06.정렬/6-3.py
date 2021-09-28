import sys
sys.stdin = open('input3.txt')

#################### 방법 1 ####################
# N, K = map(int, input().split())
# list_A = list(map(int, input().split()))
# list_B = list(map(int, input().split()))

# cnt = 0
# while cnt != K:  # 바꿔치기 횟수의 최대 = K
# 	min_idx = list_A.index(min(list_A))  # list_A에서 가장 작은 값과
# 	max_idx = list_B.index(max(list_B))  # list_B에서 가장 큰 값의 인덱스를 구해서
# 	if list_A[min_idx] < list_B[max_idx]:
# 		list_A[min_idx], list_B[max_idx] = list_B[max_idx], list_A[min_idx]  # 둘의 값을 swap
# 		cnt += 1
# 	else:
# 		break
# print(sum(list_A))


#################### 방법 2 ####################
N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 오름차순 정렬
b.sort(reverse=True)  # 내림차순 정렬

for i in range(K):  # K번 반복
	if a[i] < b[i]:  # 작을때만 교체
		a[i], b[i] = b[i], a[i]
	else:
		break

print(sum(a))

"""
배열 A에서 가장 작은 원소를 골라서 배열 B의 가장 큰 원소와 교체
단!!! 배열 A의 가장 작은 원소가 배열 B의 가장 큰 원소보다 작을때만 교체 수행!!!
1. 배열 A를 오름차순 정렬
2. 배열 B를 내림차순 정렬
3. 첫번째 인덱스부터 비교하면서 A 원소가 B 원소보다 작을 때만 교체 수행
"""

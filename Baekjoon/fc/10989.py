import sys
sys.stdin = open('input_files/10989.txt')

#################### 방법 1 ####################
# 시간초과
N = int(input())
numbers = sorted(list(int(input()) for _ in range(N)))
print(numbers)
for i in numbers:
    print(i)


#################### 방법 2 ####################
import sys

N = int(sys.stdin.readline())
array = [0] * 10001
for i in range(N):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[j]):
            print(i)


"""
- 파이썬은 기본적으로 1초에 약 2천만번정도 연산 가능
- 기본 정렬 알고리즘은 O(nlogn)의 시간복잡도를 가짐
- 때문에 천만 이상의 수가 들어오면 시간초과 남
- 다른 풀이방법 사용 필요: 계수 정렬 알고리즘 (counting sort)
1. 배열의 인덱스를 특정 데이터의 값으로 여기는 정렬 방법
2. 배열의 크기는 데이터 범위를 포함할 수 있도록 설정
3. 데이터가 등장한 횟수를 세기
"""
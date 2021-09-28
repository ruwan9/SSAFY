import sys
sys.stdin = open('input11-1.txt')

#################### 방법 1 ####################
N = int(input())
fears = list(map(int, input().split()))
fears.sort()  # 오름차순 정렬

res = 0  # 총 그룹 수
cnt = 0  # 모험가 수
for i in fears:  # 공포도를 낮은 것부터 하나씩 확인
    cnt += 1  # 모험가 추가
    if cnt >= i:  # 모험가 수가 공포도 이상이라면 그룹 추가(res += 1), 모험가 수 초기화(cnt = 0)
        res += 1
        cnt = 0
    
print(res)

"""
최소한의 모험가 수만 포함하여 그룹을 결성하기

1. 오름차순 정렬
2. 모험가 수와 공포도를 확인하며 비교
3. 모험가 수 >= 공포도가 되는 순간 그룹 결성(res += 1), 모험가 수 초기화(cnt = 0)
"""
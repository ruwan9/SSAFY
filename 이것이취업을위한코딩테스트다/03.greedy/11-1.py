import sys
sys.stdin = open('input11-1.txt')

N = int(input())
fears = list(map(int, input().split()))
fears.sort()  # 오름차순 정렬

res = 0  # 총 그룹 수
cnt = 0  # 모험가 수
for i in fears:
    cnt += 1
    if cnt >= i:
        cnt = 0
        res += 1
    
print(res)

"""
1. 오름차순 정렬
2. 모험가 수와 공포도를 확인하며 비교
3. 모험가 수 >= 공포도가 되는 순간 그룹 결성(res += 1), 모험가 수 초기화(cnt = 0)
"""
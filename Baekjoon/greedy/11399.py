import sys
sys.stdin = open('11399_input.txt')

N = int(input())
times = list(map(int, input().split()))
times.sort()

cnt = 0
for i in range(N):
    cnt += times[i] * (N-i)

print(cnt)

"""
1. 오름차순으로 정렬
2. 답을 구하기 위해 2중 for문을 돌릴까 하다가

3. times[0]은 N-0번, times[1]은 N-1번 ... 
    -> times[i]는 N-i번 더해지는 규칙을 찾아 cnt에 더해줌
"""
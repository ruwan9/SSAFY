import sys
sys.stdin = open('1931_input.txt')


def greedy(times):
    cnt = 0
    start_time = 0

    for time in times:
        if time[0] >= start_time:
            start_time = time[1]
            cnt += 1
    return cnt


N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
print(sorted(times))

# 시작시간 기준 1차 정렬
times = sorted(times, key=lambda time:time[0])
print(times)
# 종료시간 기준 2차 정렬
times = sorted(times, key=lambda time:time[1])
print(times)
print(greedy(times))

"""
1. 시작시간 기준으로 정렬하고
2. 종료시간 기준으로 한 번 더 정렬하면 시작과 종료 시간이 겹치는 문제 해결 가능 
"""







# N = int(input())

# times = [list(map(int, input().split())) for _ in range(N)]
# times.sort()

# ans = 1
# for i in range(N-1):
#     end_time = times[i][1]
#     cnt = 1
#     for j in range(i+1, N):
#         if times[j][0] >= end_time:
#             cnt += 1
#             end_time = times[j][1]

#     if cnt > ans:
#         ans = cnt

# print(ans)

"""
첫번째 풀이인데 for문을 두번 돌려서 그런지 시간초과났다...
"""


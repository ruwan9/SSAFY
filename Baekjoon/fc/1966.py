import sys
sys.stdin = open('1966_input.txt')

#################### 방법 1 ####################
# T = int(input())

# for tc in range(T):
#     N, M = map(int, input().split())
#     imp = list(map(int, input().split()))
#     idx = [i for i in range(N)]

#     for i in range(N):
#         while imp[i] != max(imp[i:]):
#             imp.append(imp.pop(i))  # 뒤에 배치하고
#             idx.append(idx.pop(i))  # index도 뒤로 밀어주기

#     print(idx.index(M)+1)


#################### 방법 2 ####################
tc = int(input())

for _ in range(tc):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]  # enumerate 활용, tuple형식으로 index 번호 저장

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
            
"""
1. 가장 큰 수가 앞에 올때까지 회전 후 추출
2. 가장 큰 수가 M이면서 가장 앞에 있을 때 종료
"""
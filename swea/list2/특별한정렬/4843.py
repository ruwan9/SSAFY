#################### 방법 1. ####################
# deque 사용
import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))
    # deque에 넣어주기
    deq = deque(numbers)

    ans = []
    while deq:
        # 큰 수, 작은 수 번갈아서 ans에 넣어주기
        ans.append(deq.pop())
        ans.append(deq.popleft())

    print(f'#{tc}', *ans[:10])


#################### 방법 2. ####################
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = []

    for i in range(int((N+1)/2)):
        ans.append(lst.pop(-1))
        ans.append(lst.pop(0))

    result = ' '.join(map(str, ans[:10]))

    print(f'#{tc} {result}')


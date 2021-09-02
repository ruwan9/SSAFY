import sys
sys.stdin = open('input4.txt')

# 1.
N, K = map(int, input().split())

cnt = 0
while True:
    if N == 1:
        break
    else:
        if not N % K:
            N = N//K
            cnt += 1
        else:
            N -= 1
            cnt += 1

print(cnt)


# 2.
N, K = map(int, input().split())
result = 0

while True:
    # N == (K로 나누어 떨어지는 수) 가 될때까지 1씩 빼기
    target = (N//K) * K
    result += (N - target)
    N = target
    
    # N이 K보다 작을 때(더이상 나눌 수 없을 때) break
    if N < K:
        break
    
    # K로 나누기
    result += 1
    N //= K

# 마지막으로 남은 수에서 1씩 빼기
result += (N-1)
print(result)
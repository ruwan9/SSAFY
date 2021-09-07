N = 18
# N = int(input())
cnt = 0
while N >= 0:
    if N%5 == 0:
        cnt += N//5
        print(cnt)
        break
    else:
        N -= 3  # 5로 나누어 떨어지지 않으면 3씩 빼기
        cnt += 1

if N < 0:
    print(-1)

"""
1. 처음에는 5의 배수, 3의 배수로 나누어 생각을 하다 너무 경우의수가 많아져서 복잡해졌다.

2. 가장 큰 수인 5로 나누어 떨어지는 경우를 먼저 조건문에 두고
3. 5로 안나누어지면 3씩 빼가며 N값을 줄여나갔다.
"""
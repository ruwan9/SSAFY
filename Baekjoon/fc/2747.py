# n = int(input())

n = 10

# 재귀 사용 - 런타임 에러
def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(n))


# dp 사용 - 런타임 에러
n = 10
d = [0] * (n+1)
d[1] = 1
d[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])


# memoization 사용 - 통과
n = 10
d = [0]*(n+1)
def fibo_dp(num):
    if num == 1 or num == 2:
        return 1
    if d[num] != 0:
        return d[num]

    d[num] = fibo_dp(num-1) + fibo_dp(num-2)
    return d[num]

print(fibo_dp(n))


# 반복문 사용 - 통과
n = 10
a, b = 0, 1
while n > 0:
    a, b = b, a+b
    n -= 1

print(a)
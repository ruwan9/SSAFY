n = 3

# 런타임 에러
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


print(fibo(5) % 1234567)


# 런타임 에러 나서 dp 사용
n = 5
d = [0] * (n+1)

def fibo_dp(x):
    d[1] = 1
    d[2] = 1

    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]


fibo_dp(n)
print(d[-1] % 1234567)



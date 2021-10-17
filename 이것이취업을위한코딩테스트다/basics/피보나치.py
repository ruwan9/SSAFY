# 반복
n = 6
a, b = 0, 1
while n > 0:
    a, b = b, a+b
    n -= 1
print(a)


# 재귀
n = 6
def fibo_recur(n):
    if n <= 2:
        return 1
    return fibo_recur(n-1) + fibo_recur(n-2)
print(fibo_recur(n))


# dp - memoization
n = 6
d = [0] * (n+1)
def fibo_memo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]

    d[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return d[n]
print(fibo_memo(n))



# dp - bottom up
n = 6
d = [0] * (n+1)

d[1] = 1
d[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
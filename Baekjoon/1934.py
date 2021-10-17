# 최대공약수
def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def LCM(a, b):
    return a * b // GCD(a, b)


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(LCM(a, b))

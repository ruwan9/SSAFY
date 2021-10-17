a, b = 24, 18

#################### 방법 1 ####################
# 런타임 에러
def div(num):
    lst = []
    for i in range(1, num//2):
        if not num % i:
            lst.append(i)
            lst.append(num//i)
    return sorted(list(set(lst)))

lst_a = div(a)
lst_b = div(b)

div_lst = []
for i in lst_a:
    if i in lst_b:
        div_lst.append(i)

GCD = div_lst[-1]
LCM = int(a/GCD * b/GCD * GCD)
print(GCD)
print(LCM)

#################### 방법 2 ####################
# 유클리드 호제법
a, b = 24, 18


# 최대공약수
def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def LCM(a, b):
    return a * b // GCD(a, b)

print(GCD(a, b))
print(LCM(a, b))
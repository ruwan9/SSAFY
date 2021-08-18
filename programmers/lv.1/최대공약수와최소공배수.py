n = 3
m = 12

# 1
def gcd(n, m):  # 최대공약수
    if n < m:
        (n, m) = (m, n)
    
    while m != 0:
        (n, m) = (m, n%m)  # 유클리드 호제법 : 나머지 이용
    
    return n

def solution(n, m):
    return [gcd(n, m), int((n * m) / gcd(n, m))]  # 최소공배수 = 두 수를 곱한값을 최대공약수로 나눈 값

print(solution(n, m))

# 2
def solution2(n, m):
    answer = []
    list_n = [] # n 약수
    list_m = [] # m 약수
    g_c = [] #최대공약수
    max_num = [] # 최대공약수
    # n의 약수 리스트
    for i in range(1, n+1) :
        if n%i == 0 :
            list_n.append(i)
    # m의 약수 리스트
    for j in range(1, m+1) :
        if m%j == 0 :
            list_m.append(j)
    
    for k in list_n :
        if k in list_m :
            max_num.append(k)
    g_c = max(max_num)

    l_c = int(n * m / g_c)

    return [g_c, l_c]
print(solution2(n, m))
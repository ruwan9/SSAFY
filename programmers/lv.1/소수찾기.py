n = 5

# 1
def is_prime(num): 
    i = 2
    while i < num:
        if num % i == 0:
            return False
        else:
            i += 1
    return True

def solution(n):
    cnt = 0
    for i in range(2, n+1):
        if is_prime(i):
            cnt += 1

    return cnt

# 2
def solution(n):
    num = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)


# 3
def prime_list(n):
    sieve = [True] * n  # 체 초기화

    m = int(n ** 0.5)  # 확인할 범위 (2부터 m까지)

    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):  # i다음부터 n까지 i의 배수 제거
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

print(prime_list(9))
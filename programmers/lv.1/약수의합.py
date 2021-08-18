n = 12

# 1
def solution(n):
    # 초기화
    i = 1
    ans = 0

    # 1부터 n까지 숫자 중 약수가 있는지 확인
    while i <= n:
        if n % i == 0:
            ans += i
            i += 1
        else:
            i += 1
    return ans

# 2
def sum_divisor(num):
    return sum([i for i in range(1, num+1) if num % i == 0])

print(sum_divisor(5))
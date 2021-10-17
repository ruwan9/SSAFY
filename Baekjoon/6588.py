import sys
sys.stdin = open('input_files/6588.txt')
import math


# 소수판별 함수
def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


while True:
    n = int(input())
    if n == 0:
        break
    ans = []
    for i in range(2, n):
        if is_prime(i) and is_prime(n-i):
            ans.append(i)
            break

    if ans:
        print(f'{n} = {ans[0]} + {n-ans[0]}')
    else:
        print("Goldbach's conjecture is wrong.")


# 에라토스테네스의 체
def find_prime(n):
    prime = []
    array = [True] * (n + 1)  # 처음엔 모든 수가 소수(True)인 것으로 초기화

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True:  # i가 소수인 경우 (남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    # 모든 소수 출력
    for i in range(2, n + 1):
        if array[i]:
            prime.append(i)

    return prime



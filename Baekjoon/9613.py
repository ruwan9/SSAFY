import sys
sys.stdin = open('input_files/9613.txt')


# 최대공약수
def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a


n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))
    n = data[0]
    numbers = data[1:]

    lst = []
    for i in range(n-1):
        for j in range(i+1, n):
            lst.append(GCD(numbers[i], numbers[j]))

    print(sum(lst))

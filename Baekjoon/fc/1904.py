import sys
sys.stdin = open('input_files/1904.txt')

n = int(input())

# 메모리 초과
d = [0] * (n+1)

d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n] % 15746)


# 런타임 에러
# n == 1일 때 오류 발생 가능
# 다음부터 d를 초기화할 때 [0] * (n+5)같이 넉넉하게 하자...
d = [0] * (n+1)

d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 15746

print(d[n])


# d의 크기를 입력의 최대값보다 1 큰 1000001로 만들고
# 미리 15746을 나눈 나머지를 받아 해결
d = [0] * 1000001
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 157456

print(d[n])
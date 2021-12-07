#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')


#################### 방법 2. ####################
# 방법 1의 if-else 구문을 expression으로
import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    str1, str2 = input(), input()
    print(f'#{t}', 1 if str1 in str2 else 0)

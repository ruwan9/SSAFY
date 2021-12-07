#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = input()

    ans = 0
    for char in str1:
        if str2.count(char) >= ans:
            ans = str2.count(char)

    print(f'#{tc} {ans}')


#################### 방법 2. ####################
# dict 이용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    count_dict = {}
    for i in range(len(str1)):
        count_dict[str1[i]] = str2.count(str1[i])

    print(f'#{tc} {max(count_dict.values())}')
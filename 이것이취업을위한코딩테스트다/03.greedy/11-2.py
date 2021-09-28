import sys
sys.stdin = open('input11-2.txt')

#################### 방법 1 ####################
# number = str(input())
# numbers = []
# for i in range(len(number)):
#     # 0인 경우 제외
#     if int(number[i]) == 0:
#         pass
#     # 그 외의 숫자 리스트에 추가
#     else:
#         numbers.append(int(number[i]))

# ans = numbers[0]
# for i in numbers[1:]:
#     # 1인 경우 더하기
#     if i == 1:
#         ans += 1
#     # 그 외는 곱하기
#     else:
#         ans *= i

# print(ans)


#################### 방법 2 ####################
data = input()
res = int(data[0])  # 첫번째 문자를 숫자로 변경하여 대입

for i in range(1, len(data)):
    num = int(data[i])  # 숫자로 변경하여 변수 저장
    if num<= 1 or res <= 1:  # 두 수 중 하나라도 0 또는 1인 경우 더하기 우선 수행
        res += num
    else:  # 나머지는 곱하기 수행
        res *= num
print(res)

"""
0 또는 1인 경우 더하기 사용, 그 외에는 곱하기 사용
"""

#################### 방법 3 ####################
# data = input()
# print(data)

# res = int(data[0])
# for i in range(1, len(data)):
#     if res == 0 or int(data[i]) <= 1:
#         res += int(data[i])
#     else:
#         res *= int(data[i])

# print(res)
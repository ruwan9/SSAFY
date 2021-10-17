import sys
sys.stdin = open('input_files/1427.txt')

#################### 방법 1 ####################
# N = input()
# N = sorted(N, reverse=True)
# print(''.join(N))



#################### 방법 2 ####################
array = input()

for i in range(9, -1, -1):  # 9부터 0까지 역순으로
    for j in array:
        if int(j) == i:
            print(i, end='')
"""
1. 자릿수를 기준으로 정렬 -> 9부터 0까지 확인
2. 각 숫자에 대해 해당 숫자의 개수를 계산하여 출력
"""
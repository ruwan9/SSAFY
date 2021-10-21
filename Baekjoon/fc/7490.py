import sys
sys.stdin = open('input_files/7490.txt')
import copy


# 가능한 연산자 리스트 경우들
def recur(array, n):
    # 종료조건
    if len(array) == n:
        operators_lst.append(copy.deepcopy(array))
        return

    array.append(' ')
    recur(array, n)
    array.pop()

    array.append('+')
    recur(array, n)
    array.pop()

    array.append('-')
    recur(array, n)
    array.pop()


T = int(input())
for _ in range(T):
    N = int(input())
    # 수 리스트
    numbers = [i for i in range(1, N+1)]
    # 연산자 리스트
    operators_lst = []
    recur([], N-1)  # 수 리스트의 갯수보다 1개 적은 연산자 갯수가 필요

    for operators in operators_lst:
        string = ''
        for i in range(N-1):
            string += str(numbers[i]) + operators[i]
        string += str(numbers[-1])  # 마지막 숫자 더해주는거 잊지 말아야 함
        if eval(string.replace(' ', '')) == 0:  # 공백일 때 제거
            print(string)
    print()
"""
1. 범위가 3 <= N <= 9 이므로 완전탐색 사용 가능
2. 수 리스트, 연산자 리스트를 분리하여 모든 경우의 수 계산
    - 가능한 모든 경우의 수를 고려, 연산자 리스트를 만든다
3. eval()함수를 이용, 문자열 형태의 표현식을 계산
    - eval('2+3') = 5
"""
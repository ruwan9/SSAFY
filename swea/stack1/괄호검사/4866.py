#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')


def check(data):
    stack = []  # 괄호 담을 스택

    for char in data:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif char == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0

    return 1 if not stack else 0


T = int(input())
for tc in range(1, T+1):
    print(f"#{tc}", check(input()))



#################### 방법 2. ####################
import sys
sys.stdin = open('input.txt')


def solution(sentence):
    stack = []

    for char in sentence:
        if char in ('(', '{'):
            stack.append(char)
        elif char in (')', '}'):
            # 여는 괄호가 없는데 닫는 괄호가 온 경우
            if not stack:
                return 0

            x = stack.pop()
            # 일치하지 않는 경우
            if char == ')' and x != '(' or char == '}' and x != '{':
                return 0

    # 반복문 다 돌렸는데 stack 에 괄호가 남아있는 경우
    return 0 if stack else 1


for t in range(1, int(input())+1):
    print(f'#{t} {solution(input())}')
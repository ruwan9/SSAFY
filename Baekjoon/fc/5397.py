import sys
sys.stdin = open('input_files/5397.txt')

T = int(input())

for tc in range(T):
    password = input()

    lstack = []
    rstack = []

    for i in password:
        if i == '-':
            if lstack:
                lstack.pop()
        elif i == '<':
            if lstack:
                rstack.append(lstack.pop())
        elif i == '>':
            if rstack:
                lstack.append(rstack.pop())
        else:
            lstack.append(i)
    lstack.extend(reversed(rstack))

    print(''.join(lstack))


"""
1. 스택 2개를 만들고 두 개의 중간 지점을 커서로 간주
2. 문자 입력 시 왼쪽 스택에 원소 삽입
3. '-' 입력: 왼쪽 스택에서 원소 삭제
4. '<' 입력: 왼쪽 스택에서 오른쪽 스택으로 원소 이동
5. '>' 입력: 오른쪽 스택에서 왼쪽 스택으로 원소 이동
6. 최종 출력 시 rstack의 값은 뒤집어서 더해주어야 함
"""
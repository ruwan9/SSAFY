import sys
sys.stdin = open('9012_input.txt')

T = int(input())

for _ in range(T):
    lst = input()
    stack = []

    ans = ''
    i = 0
    while i < len(lst):
        if lst[i] == '(':
            stack.append(lst[i])
            i += 1

        else:
            if len(stack) == 0 :
                ans = 'NO'
                break
            else: 
                stack.pop()
                i += 1

    if len(stack) == 0 and ans != 'NO':
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)

    """
    지저분한 코드...
    '('일 때 stack에 추가하고
    ')'일 때 stack에서 하나씩 빼기

    다 확인하기 전에 stack = []가 되면 'NO'
    다 확인 후 stack = []가 되면 'YES'
    다 확인 후 stack에 남은 값이 있으면 'NO' 
    """
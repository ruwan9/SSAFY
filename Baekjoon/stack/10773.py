import sys
sys.stdin = open('10773_input.txt')

K = int(input())
nums = list(int(input()) for _ in range(K))
stack = []

for num in nums:
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
    
print(sum(stack))

"""
입력받은 숫자가 0이 아니면 stack에 추가하고
0이면 stack에서 위에서부터 하나씩 빼주기
"""
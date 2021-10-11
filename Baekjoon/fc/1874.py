import sys
sys.stdin = open('input_files/1874.txt')

#################### 방법 1 ####################
n = int(input())

stack = []
count = 1
result = []

for i in range(1, n+1):
    data = int(input())  # 입력 받은 데이터에 도달할 때까지 삽입
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    # 빼낼 때 내림차순을 유지하는지 확인
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)  # 종료

print('\n'.join(result))

"""
1. 특정 수에 도달할 때까지 스택에 삽입
2. 연달아 빼낼 때 내림차순을 유지하는지 확인

3. exit(0) 사용해서 종료해버리기
"""


#################### 방법 2 ####################

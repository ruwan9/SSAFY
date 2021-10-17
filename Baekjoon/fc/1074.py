import sys
sys.stdin = open('input_files/1074.txt')

# 다시 풀어보기
def solve(n, x, y):
    global result

    # 종료조건
    if n == 2:
        if x == r and y == c:
            print(result)
            return
        result += 1

        if x == r and y+1 == c:
            print(result)
            return
        result += 1

        if x+1 == r and y == c:
            print(result)
            return
        result += 1

        if x+1 == r and y+1 == c:
            print(result)
            return
        result += 1
        return

    solve(n/2, x, y)
    solve(n/2, x, y+n/2)
    solve(n/2, x+n/2, y)
    solve(n/2, x+n/2, y+n/2)


N, r, c = map(int, input().split())
result = 0
solve(2**N, 0, 0)


"""
1. 크기는 절반으로 줄이고
2. 위치는 크기의 절반만큼 더해줘서 이동
"""
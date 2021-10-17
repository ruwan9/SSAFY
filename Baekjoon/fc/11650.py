import sys
sys.stdin = open('input_files/11650.txt')


N = int(input())
data = sorted(list(list(map(int, input().split())) for _ in range(N)))
for i in data:
    print(*i)

"""
기본 정렬 라이브러리는 기본적으로 인덱스 순서대로 오름차순 정렬
"""
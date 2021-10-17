import sys
sys.stdin = open('input_files/1920.txt')

N = int(input())
numbers1 = set(map(int, input().split()))
M = int(input())
numbers2 = list(map(int, input().split()))

for i in numbers2:
    if i in numbers1:
        print(1)
    else:
        print(0)

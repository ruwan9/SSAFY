import sys
sys.stdin = open('input3.txt')

start = input()
row = int(start[1])
col = int(ord(start[0]) - ord('a') + 1)  # a~h에 해당하는 열을 1~8로 바꾸어 저장, 숫자형

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

cnt = 0
for step in steps:
    x = step[0]
    y = step[1]
    if row + x >= 1 and col + y >= 1 and row + x <= 8 and col + y <= 8:
        cnt += 1

print(cnt) 

"""
* ord() 사용해서 문자에 해당하는 ASCII code값을 가져오고 'a'에 해당하는 ASCII code값을 빼줘서 문자를 숫자로 변환시켰다.

1. 이동할 수 있는 전체 경우를 넣은 steps 리스트 제작
2. 각 경우에 대하여 정원 안에 있는 경우에만 cnt에 1 추가

4-1.py와는 다르게 dx, dy를 사용하지 않고 리스트를 활용하여 경우의수를 판단
"""
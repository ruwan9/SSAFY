import sys
sys.stdin = open('2309_input.txt')

lst = [int(input()) for _ in range(9)]

minus = sum(lst) - 100

for i in range(8):
    for j in range(i+1, 9):
        if lst[i] + lst[j] == minus:
            lier_1 = lst[i]
            lier_2 = lst[j]

lst.remove(lier_1)
lst.remove(lier_2)

lst.sort()

for i in lst:
    print(i)
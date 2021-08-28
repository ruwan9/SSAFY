n = 1

# import sys
# n = int(input())

cnt = 0
ans = []
for i in range(n, n//2-1, -1):
    lst = [n, i]
    j = 0
    while lst[j] - lst[j+1] >= 0:
        lst.append(lst[j]-lst[j+1])
        j += 1
    if cnt < len(lst):
        cnt = len(lst)
        ans = lst[:]
print(cnt)
print(* ans)

# 2.
count = 0
answer = []
for i in range(n+1):
    lst = [n, i]
    j = 0

    while True:
        temp = lst[j] - lst[j+1]
        if temp <= -1:
            break
        lst.append(temp)
        if count < len(lst):
            count = len(lst)
            answer = lst
        j += 1
print(count)
print(*answer)

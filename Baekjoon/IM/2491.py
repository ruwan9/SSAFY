N = 9
arr = [4, 1, 3, 3, 2, 2, 9, 2, 3]


cnt = 1
ans = 1

for i in range(1, N):
    if arr[i-1] >= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt

cnt = 1
for j in range(1, N):
    if arr[j-1] <= arr[j]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt

print(ans)




N = int(input())
arr = list(map(int, input().split()))

cnt_up = 0
cnt_down = 0
lst = []

i = 1
while i < N:
    if arr[i-1] <= arr[i]:
        cnt_up += 1
        i += 1
        lst.append(cnt_up)
    else:
        i += 1
        cnt_up = 0

j = 1
while j < N:
    if arr[j-1] >= arr[j]:
        cnt_down += 1
        j += 1
        lst.append(cnt_down)
    else:
        j += 1
        cnt_down = 0

ans = max(lst) + 1
print(ans)
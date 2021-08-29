def length(axis):
    length = []
    for i in range(len(axis)-1):
        length.append(axis[i+1] - axis[i])
    return length

row, col = map(int, input().split())
n = int(input())
axis_lst = [list(map(int, input().split())) for _ in range(n)]

row, col = 10, 8 
n = 3
axis_lst = [[0, 3], [1, 4], [0, 2]] 

x = [0, col]
y = [0, row]
ans = []

for i in axis_lst:
    if i[0] == 0:
        x.append(i[1])
    else:
        y.append(i[1])
x.sort()
y.sort()

for i in length(x):
    for j in length(y):
        ans.append(i*j)

print(max(ans))
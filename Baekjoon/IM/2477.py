import sys
sys.stdin = open('2477_input.txt')

K = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
print(lst)
w = 0
w_idx = 0
h = 0
h_idx = 0

for i in range(6):
    if lst[i][0] == 1 or lst[i][0] == 2:
        if w < lst[i][1]:
            w = lst[i][1]
            w_idx = i
    if lst[i][0] == 3 or lst[i][0] == 4:
        if h < lst[i][1]:
            h = lst[i][1]
            h_idx = i

sub_w = abs(lst[(w_idx-1)%6][1] - lst[(w_idx+1)%6][1])
sub_h = abs(lst[(h_idx-1)%6][1] - lst[(h_idx+1)%6][1])

ans = ((w*h) - (sub_w*sub_h)) * K
print(ans)



# point_lst = [[] for _ in range(6)]

# x, y = 0, 0
# for i in range(6):
#     if lst[i][0] == 4:
#         y += lst[i][1]
#     elif lst[i][0] == 3:
#         y -= lst[i][1]
#     elif lst[i][0] == 2:
#         x -= lst[i][1]
#     elif lst[i][0] == 1:
#         x += lst[i][1]

#     point_lst[i].append(x)
#     point_lst[i].append(y)

# x_lst = []
# y_lst = []
# for i in range(6):
#     if point_lst[i][0] != 0:
#         x_lst.append(abs(point_lst[i][0]))
#     if point_lst[i][1] != 0:
#         y_lst.append(abs(point_lst[i][1]))

# print(((max(x_lst) * max(y_lst)) - (max(x_lst)-min(x_lst)) * min(y_lst))*K)
scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
col_lst = [[] for _ in range(len(scores))]
grade = []

for i in range(len(scores)):
    for j in range(len(scores)):
        col_lst[i].append(scores[j][i])

for i in range(len(col_lst)):
    for j in range(len(col_lst)):
        if i == j and col_lst[i][j] == max(col_lst[i]) and col_lst[i].count(max(col_lst[i])) == 1:
            col_lst[i].remove(col_lst[i][i])
        elif i == j and col_lst[i][j] == min(col_lst[i]) and col_lst[i].count(min(col_lst[i])) == 1:
            col_lst[i].remove(col_lst[i][i])

lst = []
for i in range(len(col_lst)):
    ans = 0
    for j in range(len(col_lst[i])):
        ans += col_lst[i][j]
    lst.append(ans/len(col_lst[i]))

for i in lst:
    if i >= 90:
        grade.append('A')
    elif 80 <= i < 90:
        grade.append('B')
    elif 70 <= i < 80:
        grade.append('C')
    elif 50 <= i < 70:
        grade.append('D')
    else:
        grade.append('F')

ans = ''
for i in grade:
    ans += i

print(ans)
priorities = [2, 1, 3, 2]
location = 2

# 1. enumerate 이용
idx_p = list(enumerate(priorities))
ans = ''

i = 0
while i < len(idx_p):
    if idx_p[i][1] < max(priorities[i:]):
        idx_p.append(idx_p.pop(i))
        priorities.append(priorities.pop(i))
    else:
        i += 1

for i in range(len(priorities)):
    if idx_p[i][0] == location:
        ans = i+1

print(ans)


# 2. 
# ans = 0
# idx_p = [c for c in range(len(priorities))]

# i = 0
# while True :
#     if priorities[i] < max(priorities[i+1:]) :
#         priorities.append(priorities.pop(i))
#         idx_p.append(idx_p.pop(i))  # 뒤로 보내는 문서의 위치를 따라 보내주기
#     else :
#         i += 1

#     if priorities == sorted(priorities, reverse = True) : 
#         break

# print(idx_p)
# ans = idx_p.index(location) + 1
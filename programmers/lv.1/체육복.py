n = 5 
lost = [2, 4]  # 체육복 안가져온 학생 번호
reserve = [1, 3, 5]  # 여벌 체육복 가져온 학생 번호

students = [i for i in range(1, n+1)]

lost_set = set(lost) - set(reserve)
reserve_set = set(reserve) - set(lost)

for i in reserve_set:
    if i-1 in lost_set:
        lost_set.remove(i-1)
    elif i+1 in lost_set:
        lost_set.remove(i+1)

ans = n - len(lost_set)
print(ans)

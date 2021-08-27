import sys
sys.stdin = open('1244_input.txt')

switch_num = int(input())
onoff = [0]
onoff.extend(list(map(int, input().split())))
student_num = int(input())
students = [list(map(int, input().split())) for _ in range(student_num)]

onoff = [0, 0, 1, 0, 1, 0, 0, 0, 1]
students = [[1, 3], [2, 4]]

for student in students:
    gender, switch = student[0], student[1]
    if gender == 1:
        for i in range(len(onoff)):
            if i % switch == 0 and onoff[i] == 0:
                onoff[i] = 1
            elif i % switch == 0 and onoff[i] == 1:
                onoff[i] = 0

    elif gender == 2:
        onoff = onoff[1:]
        print(onoff)
        i = 0
        while onoff[switch-1-i] == onoff[switch-1+i] and 0<=switch-1-i and switch_num >= switch-1+i:
            if  onoff[switch-1-i] == 0:
                onoff[switch-1-i] = 1
                onoff[switch-1+i] = 1
                i += 1
            elif onoff[switch-1-i] == 1:
                onoff[switch-1-i] = 0
                onoff[switch-1+i] = 0
                i += 1
print(*onoff)
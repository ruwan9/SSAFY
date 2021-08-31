import sys
sys.stdin = open('1244_input.txt')

# switch_num = int(input())
# onoff = [0]
# onoff.extend(list(map(int, input().split())))
# student_num = int(input())
# students = [list(map(int, input().split())) for _ in range(student_num)]

# for student in students:
#     gender, switch = student[0], student[1]
#     if gender == 1:
#         for i in range(len(onoff)):
#             if i % switch == 0 and onoff[i] == 0:
#                 onoff[i] = 1
#             elif i % switch == 0 and onoff[i] == 1:
#                 onoff[i] = 0

#     elif gender == 2:
#         onoff = onoff[1:]
#         i = 0
#         while onoff[switch-1-i] == onoff[switch-1+i] and 0<=switch-1-i < switch_num:
#             if  onoff[switch-1-i] == 0:
#                 onoff[switch-1-i] = 1
#                 onoff[switch-1+i] = 1
#                 i += 1
#             elif onoff[switch-1-i] == 1:
#                 onoff[switch-1-i] = 0
#                 onoff[switch-1+i] = 0
#                 i += 1

# for i in range(0, switch_num, 20):
#     print(*onoff[i:i+20])




n = int(input())
onoff = list(map(int, input().split()))
onoff.insert(0, 0)
student_num = int(input())
for _ in range(student_num):
    gender, switch = map(int, input().split())

    if gender == 1:  # 남자
        for i in range(1, len(onoff)):
            if i%switch == 0:
                if onoff[i] == 0:
                    onoff[i] = 1
                elif onoff[i] == 1:
                    onoff[i] = 0
    
    
    elif gender == 2:  # 여자
        if onoff[(switch)] == 0:
            onoff[(switch)] = 1
        else:
            onoff[(switch)] = 0
        l = switch-1
        r = switch+1

        while l>=1 and r <= n and onoff[l] == onoff[r]:
            if onoff[l] == 0:
                onoff[l] = 1
                onoff[r] = 1
            elif onoff[l] == 1:
                onoff[l] = 0
                onoff[r] = 0
            l -= 1
            r += 1
            if l<1 or r > n:
                break 

ans = onoff[1:]

for i in range(0, n, 20):
    print(*ans[i:i+20])

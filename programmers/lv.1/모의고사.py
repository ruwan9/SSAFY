answers = [1,3,2,4,2, 1, 2, 3, 4, 5]	

# def solution(answers):
#     ans = []

#     std_1 = [1, 2, 3, 4, 5]
#     std_2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     std_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
#     cnt_1 = 0
#     cnt_2 = 0
#     cnt_3 = 0
    
#     for i in range(len(answers)):
#         if answers[i] == std_1[i%5]:
#             cnt_1 += 1
#         if answers[i] == std_2[i%5]:
#             cnt_2 += 1
#         if answers[i] == std_3[i%5]:
#             cnt_3 += 1

#     max_cnt = max(cnt_1, cnt_2, cnt_3)

#     if max_cnt == cnt_1:
#         ans.append(1)
#     if max_cnt == cnt_2:
#         ans.append(2)
#     if max_cnt == cnt_3:
#         ans.append(3)

#     return ans
# print(solution(answers))

# 2.
def score(student, answers):
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == student[i%len(student)]:
            cnt += 1
    return cnt

def solution2(answers):
    std_1 = [1, 2, 3, 4, 5]
    std_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = []
    scores = []
    scores.append(score(std_1, answers))
    scores.append(score(std_2, answers))
    scores.append(score(std_3, answers))
    print(scores)
    for i in range(3):
        if scores[i] == max(scores):
            ans.append(i+1)
    return sorted(ans)
print(solution2(answers))
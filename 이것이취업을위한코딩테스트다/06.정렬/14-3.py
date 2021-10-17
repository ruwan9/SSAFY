N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

#################### 방법 1 ####################		
people = len(stages)

# 스테이지 별 실패 인원 dic에 저장
dic = {}
for i in range(1, N+1):
    dic[i] = stages.count(i)

# 스테이지 별 실패율 fail에 저장
fail = {}
for i in range(1, len(dic)+1):
    fail[i] = dic[i]/(people)
    people -= dic[i]

# 실패율 기준으로 내림차순 정렬
sorted_fail = sorted(fail.items(), key=lambda item:item[1], reverse=True)

# 정렬된 스테이지 출력
ans = []
for i in sorted_fail:
    ans.append(i[0])
print(ans)


#################### 방법 2 ####################
def solution(N, stages):
    ans = []
    length = len(stages)

    # 스테이지 번호 1부터 N까지 증가
    for i in range(1, N+1):
        # 해당 스테이지에 머무른 사람 수
        cnt = stages.count(i)

        # 실패율
        if length == 0:
            fail = 0
        else:
            fail = cnt / length

        # 리스트에 원소 삽입
        ans.append((i, fail))
        length -= cnt
    
    #  실패율 기준, 내림차순 정렬
    ans = sorted(ans, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    ans = [i[0] for i in ans]
    return ans
print(solution(N, stages))
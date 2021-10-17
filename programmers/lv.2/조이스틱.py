name = "JAAAAN"

# 틀린 풀이
cnt = 0
i = 0
while i < len(name):
    tmp = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
    cnt += tmp
    cnt += 1
    i += 1
cnt -= 1

if name[1:].count('A') == len(name)-2:
    cnt -= (len(name)-2)

if name[-1] == 'A':
    cnt -= 1


print(cnt)



# 다른 사람 풀이
def solution(name):
    # 최소한의 조이스틱 가동 횟수
    make_name = [min(ord(i) - ord('A'), ord('Z') - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) == 0:
            break
        left, right = 1, 1
        while make_name[idx - left] == 0:
            left += 1
        while make_name[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer
print(solution(name))
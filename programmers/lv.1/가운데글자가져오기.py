s = "abcde"

def solution(s):
    if len(s) % 2:  # 홀수일 때
        return s[len(s)//2]
    else:
        return s[len(s)//2 - 1:len(s)//2 + 1]
print(solution(s))

print(s[2])
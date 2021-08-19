s = 'a234'

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() :  # 숫자인지 판별
            return True
    return False

print(solution(s))
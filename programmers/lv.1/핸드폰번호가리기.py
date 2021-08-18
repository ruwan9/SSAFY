phone_number = '01033334444'

# 1
def solution(phone_number):
    ans = ''
    for i in range(len(phone_number)-4):
        ans += '*'
    ans += phone_number[len(phone_number)-4:]
    return ans
print(solution(phone_number))

# 2
def solution2(phone_number):
    lst = list(phone_number)  # 리스트 변환

    for i in range(len(lst)-4):
        lst[i] = '*'  # 뒤 4자리 빼고 *로 치환

    return ''.join(lst)
print(solution2(phone_number))
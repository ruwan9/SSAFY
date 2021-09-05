n = 16

ans = ''
while n:
    mox, nam = divmod(n, 3)
    if nam == 0:
        ans = '4' + ans
        n = mox-1
    else:
        ans = str(nam) + ans        
        n = mox
print(ans)

"""
divmod(n, m): n을 m으로 나눈 목과 나머지를 return

string을 더할 때 앞에 더해질지, 뒤에 더해질지 신경써서 추가해주기
"""

#2.
n = 16
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer
print(solution(n))

"""
규칙을 찾아 풀기
문자열의 index 활용
"""
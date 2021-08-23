n = 45

def solution(n):
    n_three = ''
    while n > 0:
        n_three += str(n%3)  # 자연수 n을 3진법으로 돌리고 앞뒤로 뒤집기
        n = n // 3

    ans = 0
    for i in range(len(n_three)):
        ans += int(n_three[len(n_three)-1-i]) * 3**i
    
    return ans

print(solution(n))


# 2
def solution2(n):
    answer = ''

    while n > 0:			
        n, re=divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer+=str(re)
            
    return int(answer, 3)	# 3진법 answer을 10진법으로 변환
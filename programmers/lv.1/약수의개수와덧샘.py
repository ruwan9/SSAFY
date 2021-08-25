left = 13
right = 17

# # 1.
# def find_div(num):
#     cnt = 0
#     for i in range(1, num+1):
#         if not num % i:
#             cnt += 1
#     return cnt

# def solution(left, right):
#     ans = 0
#     for num in range(left, right+1):
#         if find_div(num) % 2:  # 홀수일 때
#             ans -= num
#         else:
#             ans += num

#     return ans

# 2.
def solution2(left, right):
    ans = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):	
            if i % j == 0:
                cnt +=1
        
        if cnt % 2 == 0:
            ans += i
        else:
            ans -= i
            
    return ans	

print(solution2(left, right))
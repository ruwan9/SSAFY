# citations = [3, 0, 6, 1, 5]
# citations = [88, 89]

# tc 11번 오류
# def solution(citations):
#     ans = 0
#     n = len(citations)

#     for h in range(1, n+1):
#         tmp = 0
#         for i in citations:
#             if i >= h:
#                 tmp += 1
#         if tmp >= h and n-tmp <= h:
#             ans = tmp
            
#     return ans


# tc 16번 오류
# citations = [1, 0, 0, 0]
# ans = 0
# def solution(citations):
#     for h in range(max(citations), 0, -1):
#         tmp = 0
#         for citation in citations:
#             if citation >= h:
#                 tmp += 1
#             if tmp == h:
#                 return h

# print(solution(citations))


# 정답
citations = [88, 89]
citations = [1, 0, 0, 0]
n = len(citations)
ans = 0

citations.sort()
for h in range(n):
    if citations[h] >= n-h:
        ans = n-h
    else:
        ans = 0

print(ans)





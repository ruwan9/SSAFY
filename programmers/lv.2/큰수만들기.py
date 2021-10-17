number = "99991"
k = 3

# # 시간초과
# from itertools import combinations
#
# combs = list(combinations(number, len(number)-k))
# combs.sort()
# ans = ''
# for comb in combs[-1]:
#     ans += comb
# print(ans)
ans = ''
stack = []
for num in number:
    # 비어있으면 num 채우고 다음 num으로 넘어가기
    if not stack:
        stack.append(num)
        continue

    if k > 0:
        while stack[-1] < num:
            stack.pop()
            k -= 1
            # stack 이 비거나 k가 0이 되면 끝
            if not stack or k == 0:
                break
    # 스택에 다음 num 추가
    stack.append(num)

print(stack)
for i in stack:
    ans += i
print(ans)


stack = stack[:-k] if k > 0 else stack
print(''.join(stack))


#
# stack = []
# for num in number:
#     if not stack:
#         stack.append(num)
#         continue
#     if k > 0:
#         while stack[-1] < num:
#             stack.pop()
#             k -= 1
#             if not stack or k == 0:
#                 break
#     stack.append(num)
#
# print(stack)
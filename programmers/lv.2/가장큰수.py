from itertools import permutations

numbers = [3, 30, 34, 5, 9]

# 시간초과
num = list(map(str, numbers))
perms = sorted(list(permutations(num)))
print(perms)

list(perms[-1]).sort()
print(''.join(perms[-1]))


# # 위에꺼는 시간초과나서 permutation 쓰지 않고
# num = list(map(str, numbers))
# num = sorted(num, key=lambda x: x*3, reverse=True)  # 1000 이하의 원소니까 *3만 해주면 됨
# print(''.join(num))
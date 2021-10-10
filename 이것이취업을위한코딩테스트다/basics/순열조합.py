#################### 순열 ####################
# nPr = n!/(n-r)!
# 서로 다른 n개 중 r개를 선택하는 경우의 수
# 순서 상관 있음
# [1, 2, 3] != [1, 3, 2]

# ex) 4P3
arr = [1, 2, 3, 4]
N = len(arr)
perm = []
visited = [0] * N

def permutation(idx):
    global perm
    if idx == 3:
        print(perm)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            perm.append(arr[i])
            permutation(idx+1)
            perm.pop()
            visited[i] = 0
print('4P3')
permutation(0)
#################### 조합 ####################
#nCr = n!/((n-r)!*r!)
# 서로 다른 n개 중 r개를 선택하는 경우의 수
# 순서 상관 없음
# [1, 2, 3] == [1, 3, 2]

# ex) 4C3
arr = [1, 2, 3, 4]
N = len(arr)
comb = []
visited = [0] * N

def combination(idx):
    global comb
    if idx == 3:
        print(comb)

    for i in range(idx, N):
        if visited[i] == 0:
            visited[i] = 1
            comb.append(arr[i])
            combination(idx+1)
            comb.pop()
            visited[i] = 0
print('4C3')
combination(0)
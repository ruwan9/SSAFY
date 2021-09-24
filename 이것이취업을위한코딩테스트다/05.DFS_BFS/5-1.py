import sys
sys.stdin = open('input1.txt')


N, M = map(int, input().split())  # N: 세로 길이, M: 가로 길이
graph = list(list(map(int, input())) for _ in range(N))
print(graph)

def dfs(r, c):
    if r <= -1 or r >= N or c <= -1 or c >= N:
        return False
    
    if graph[r][c] == 0:
        graph[r][c] = 1
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1


















# def dfs(r, c):
#     if r <= -1 or r >= N or c <= -1 or c >= N:
#         return False
    
#     if graph[r][c] == 0:
#         graph[r][c] = 1

#         dfs(r-1, c)
#         dfs(r, c-1)
#         dfs(r+1, c)
#         dfs(r, c+1)
#         return True
#     return False


# result = 0
# for i in range(N):
#     for j in range(M):

#         if dfs(i, j) == True:
#             result += 1

# print(result)
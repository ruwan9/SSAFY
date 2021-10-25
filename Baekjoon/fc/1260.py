import sys
sys.stdin = open('input_files/1260.txt')
from collections import deque

#################### 방법 1. ####################
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        graph[v].sort()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(M+1)


for _ in range(M):
    # 양방향 그래프
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(V)
print()
visited = [False]*(M+1)
bfs(V)


#################### 방법 2. ####################
